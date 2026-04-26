from sqlalchemy import ForeignKey, String, create_engine, select, Integer, Numeric, and_, or_
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from datetime import date
from typing import List, Optional
from decimal import Decimal
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    force=True,
)
logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    products: Mapped[List["Product"]] = relationship(back_populates="manufacturer", cascade="all, delete-orphan",
                                                     lazy="select")

    def __repr__(self):
        return f"Manufacturer id={self.id}, name={self.name}"

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id"), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    serial_number: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=False)

    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="products")

    orders: Mapped[List["Order"]] = relationship(back_populates="product", lazy="select")

    def __repr__(self):
        return f"Product {self.id} name={self.name} price={self.price}"

    def __str__(self):
        return f"{self.name} {self.category} {self.price} Руб."


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    orders: Mapped[List["Order"]] = relationship(back_populates="customer", lazy="select")

    def __repr__(self):
        return f"Customer {self.id} name={self.first_name} last_name={self.last_name} email={self.email}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    order_date: Mapped[date] = mapped_column(nullable=False)
    delivery_date: Mapped[Optional[date]] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(String(300), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="orders")
    customer: Mapped["Customer"] = relationship(back_populates="orders")

    def __repr__(self):
        return f"Order {self.id} status={self.status} order_date={self.order_date}"

    def __str__(self):
        return f"Order {self.id} status={self.status} order_date={self.order_date}"

    @property
    def is_active(self):
        active_statuses = {"Progressing", "Shipped", "Confirmed", "Pending"}
        return self.status in active_statuses


class StoreManager:
    STATUS_PROGRESSING = "Progressing"
    STATUS_SHIPPED = "Shipped"
    STATUS_DELIVERED = "Delivered"
    STATUS_CANCELED = "Canceled"

    ACTIVE_STATUSES = {STATUS_PROGRESSING, STATUS_SHIPPED, "Confirmed", "Pending"}

    def __init__(self, db_path: str):
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False, connect_args={"check_same_thread": False})
        Base.metadata.create_all(self.engine)
        logger.info(f"Connect to DB: {db_path}")

    def _get_session(self) -> Session:
        return Session(self.engine)

    def _fetch_one(self, stmt):
        try:
            with self._get_session() as session:
                result = session.scalars(stmt)
                return result
        except SQLAlchemyError as e:
            logger.error(f"ERROR request : {e}")
            raise

    def _fetch_all(self, stmt):
        try:
            with self._get_session() as session:
                result = session.scalars(stmt).all()
                return result
        except SQLAlchemyError as e:
            logger.error(f"ERRORS requests : {e}")
            raise

    def _save_object(self, obj):
        try:
            with self._get_session() as session:
                session.add(obj)
                session.commit()
                session.refresh(obj)
                session.expunge(obj)
                return obj
        except SQLAlchemyError as e:
            if "session" in locals():
                session.rollback()
            logger.error(f"ERROR save {e}")
            raise

    def _delete_object(self, obj):
        try:
            with self._get_session() as session:
                session.delete(obj)
                session.commit()
                return True
        except SQLAlchemyError as e:
            if "session" in locals():
                session.rollback()
            logger.error(f"ERROR delete {e}")
            return False

    def add_manufacturer(self, name: str) -> Manufacturer:
        if not isinstance(name, str):
            raise ValueError("Название не должно быть пустой строкой")
        manufacturer = Manufacturer(name=name.strip())
        saved_manufacturer = self._save_object(manufacturer)

        logger.info(f"Производитель добавлен {saved_manufacturer.name} {saved_manufacturer.id}")

        return saved_manufacturer

    def get_all_manufacturer(self) -> List[Manufacturer]:
        stmt = select(Manufacturer)

        return self._fetch_all(stmt)

    def find_manufacturer_by_id(self, manufacturer_id: int) -> Optional[Manufacturer]:
        if not isinstance(manufacturer_id, int) or manufacturer_id <= 0:
            raise ValueError("ID должен быть больше нуля")
        stmt = select(Manufacturer)

    def update_manufacturer(self, manufacturer_id: int, new_name: str) -> bool:
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Новое имя должно быть не пустой строкой")
        manufacturer = self.find_manufacturer_by_id(manufacturer_id)

        if not manufacturer:
            logger.warning(f"Производитель {manufacturer_id} не найден")
            return False

        old_name = manufacturer.name
        manufacturer.name = new_name.strip()

        self._save_object(manufacturer)

        logger.info(f"Производитель {manufacturer_id}, {old_name} обновлен на {new_name}")
        return True

    def _execute_query(self, stmt):
        with Session(self.engine) as session:
            result = session.execute(stmt)
            session.commit()
            return result.scalars().all() if hasattr(result, "scalars") else result.scalar_one_or_none()

    def _execute_mutation(self, obj_to_save):
        with Session(self.engine) as session:
            session.add(obj_to_save)
            session.commit()

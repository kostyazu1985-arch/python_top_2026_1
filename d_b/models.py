from sqlalchemy import ForeignKey, String, create_engine, select, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapper, Session, mapped_column, relationship
from datetime import date
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    products: Mapped[List["Product"]] = relationship(back_populates="manufacturer", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id"), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)

    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="products")


from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///products.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Product(name = {self.name}, price = {self.price}, stock = {self.stock})>"

class ProductManager:
    def __init__(self):
        pass

    def create(self, name, price, stock=0, is_available=True):
        session = Session()

        try:
            product = Product(
                name=name,
                price=price,
                stock=stock,
                is_available=is_available
            )

            session.add(product)
            session.commit()

            print(f"Товар {name} добавлен (ID={product.id})")
            return product

        except Exception as e:
            session.rollback()
            print(f"Ошибка")
            return None

        finally:
            session.close()

    def get_all(self):
        session = Session()
        products = session.query(Product).all()
        session.close()
        return products

    def get_by_id(self, product_id):
        session = Session()
        product = session.query(Product).filter(Product.id == product_id).first()
        session.close()
        return product

    def get_by_name(self, name):
        session = Session()
        product = session.query(Product).filter(Product.name == name).first()
        session.close()
        return product

    def get_out_of_stock(self, stock):
        session = Session()
        products = session.query(Product).filter(Product.stock == 0).all()
        session.close()
        return products

    def get_available(self, is_available):
        session = Session()
        products = session.query(Product).filter(Product.is_available == True).all()
        session.close()
        return products

    def get_by_price_range(self, price_min, price_max):
        session = Session()
        products = session.query(Product).filter(Product.price >= price_min, Product.price <= price_max).all()
        session.close()
        return products

    def update_price(self, product_id, new_price):
        session = Session()
        try:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                old_price = product.price
                product.price = new_price
                session.commit()
                print(f"Цена {product.name} обновлена с {old_price} на {new_price}")
                return True
            else:
                print(f"Товар с ID {product.id} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

    def update_stock(self, product_id, new_stock):
        session = Session()
        try:
            product = session.query(Product).filter(Product.stock == new_stock).first()
            if product:
                old_stock = product.stock
                product.stock = new_stock
                session.commit()
                print(f"Остаток {product.name} обновлен с {old_stock} на {new_stock}")
                return True
            else:
                print(f"Товар с ID {product_id} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

    def add_stock(self, product_id, quantity):
        session = Session()
        try:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                if quantity > 0:
                    product.stock += quantity
                    session.commit()
                    print(f" {product.name} увеличился на {quantity} всего {product.stock}")
                    return True
                else:
                    print(f"Количество должно быть положительным")
                    return False
            else:
                print(f"Товар с ID {product_id} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

    def update_available(self, product_id, is_available):
        session = Session()
        try:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                    product.is_available = is_available
                    status = "Доступно" if is_available else "Недоступно"
                    session.commit()
                    print(f"Товар {product.name} теперь {status}")
                    return True
            else:
                print(f"Товар с ID {product_id} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

    def update_full(self, product_id, **kwargs):
        session = Session()
        try:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                for key, value in kwargs.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                session.commit()
                print(f"Товар {product.name} полностью обновлен")
                return True
            else:
                print(f"Товар с ID {product_id} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

    def delete_by_id(self, product_id):
        session = Session()
        try:
            product = session.query(Product).filter(Product.id == product_id).first()
            if product:
                session.delete(product)
                session.commit()
                print(f"Товар {product.name} (ID={product_id}) удален")
                return True
            else:
                print(f"Товар с ID {product_id} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

    def delete_by_name(self, name):
        session = Session()
        try:
            product = session.query(Product).filter(Product.name == name).first()
            if product:
                session.delete(product)
                session.commit()
                print(f"Товар {product.name} удален")
                return True
            else:
                print(f"Товар с ID {name} не найден")
                return False
        except Exception as e:
            session.rollback()
            print(f"Ошибка {e}")
            return False
        finally:
            session.close()

class ProductViewer:
    def print_header(self, text):
        print(f"==={text}===")

    def print_one(self, product):
        if product:
            status = "В наличии" if product.is_available else "Нет в наличии"
            stock_info = f"{product.stock} шт" if product.stock > 0 else "0 шт"
            print(f"ID{product.id} | {product.name} | {product.price} | {stock_info} | {status}")
        else:
            print("Товар не найден")

    def print_all(self, products):
        if not products:
            print("Товар не найден")
            return
        for p in products:
            self.print_one(p)

    def print_statistics(self, products):
        if not products:
            print("Не найден")
            return

        total = len(products)
        available = sum(1 for p in products if p.is_available)
        in_stock = sum(1 for p in products if p.stock > 0)
        total_price = sum(p.stock * p.price for p in products)
        avg_price = sum(p.stock * p.price for p in products) / total

        print(f"Всегго товаров {total}")
        print(f"Доступно {available}")
        print(f"В наличии {in_stock}")
        print(f"Общая стоимость {total_price}")
        print(f"Средняя цена {avg_price}")

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    manager = ProductManager()
    viewer = ProductViewer()

    viewer.print_header("База готова")

    # manager.create("Ноутбук", 50000, stock=10)
    # manager.create("Ноутбук 16-дюймов", 80000, stock=20)
    # manager.create("Мышка", 5000, stock=100)
    # manager.create("Клавиатура", 3000, stock=80)
    # manager.create("Монитор", 15000, stock=20)
    # manager.create("Системный блок", 500000, stock=5)
    # manager.create("Роутер", 10000, stock=28)
    # manager.create("Телефон", 250000, stock=35)
    # manager.create("Планшет", 450000, stock=2)
    # manager.create("Наушники", 9000, stock=30)
    # manager.create("Часы", 8000, stock=0, is_available=False)
    # manager.create("Smart-Часы", 75000, 10, False)

    # print("Все товары")
    # products = manager.get_all()
    # viewer.print_all(products)

    # print("Обновление товаров")
    # manager.update_price(product_id=1, new_price=55555)
    # manager.add_stock(product_id=10, quantity=20)
    # manager.update_available(product_id=12, is_available=True)

    # print("Проверка")
    # products = manager.get_all()
    # viewer.print_all(products)

    # by_price = manager.get_by_price_range(10000, 100000)
    # viewer.print_all(by_price)

    # print("Удаление")
    # manager.delete_by_id(product_id=11)
    # manager.delete_by_name("Планшет")

    # products = manager.get_all()
    # viewer.print_all(products)

    # print("Статистика")
    # viewer.print_statistics(products)







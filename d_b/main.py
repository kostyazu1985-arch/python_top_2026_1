from models import StoreManager
import os

def main():
    db_path = "Mvideo.db"
    store = StoreManager(db_path)

    print(f"База данных создана по пути {os.path.abspath(db_path)}")
    # try:
    #     samsung = store.add_manufacturer("Samsung")
    #     print(f"Производитель {samsung} добавлен с id {samsung.id}")
    #     motorola = store.add_manufacturer("Motorola")
    #     print(f"Производитель {motorola} добавлен с id {motorola.id}")
    # except Exception as e:
    #     print(f"{e}")

    # try:
    #     manufacturers = store.get_all_manufacturer()
    #     print(f"Найдено {len(manufacturers)}")
    #     for manufacturer in manufacturers:
    #         print(manufacturer)
    # except Exception as e:
    #     print(f"{e}")

    # try:
    #     found = store.find_manufacturer_by_id(5)
    #     founds = store.get_all_manufacturer()
    #     print(len(founds))
    #     for m in founds:
    #         print(m)
    #     if found:
    #         print(found)
    #     else:
    #         print("Not found")
    # except Exception as e:
    #     print(f"{e}")
    #
    # try:
    #     upd = store.update_manufacturer(1, "Samsung inc")
    #     if upd:
    #         upd = store.find_manufacturer_by_id(1)
    #         print(f"Обновлен {upd}")
    #     else:
    #         print("Производитель не найден")
    # except Exception as e:
    #     print(f"{e}")

    # try:
    #     delite_man = store.delete_manufacturer(2)
    #     if delite_man:
    #         print(f"Success {delite_man}")
    #     else:
    #         print("Not found")
    # except Exception as e:
    #     print(f"{e}")

    # try:
    #     manufacturers = store.get_all_manufacturer()
    #     for manufacturer in manufacturers:
    #         print(manufacturer.id)
    #         store.delete_manufacturer(manufacturer.id)
    #
    # except Exception as e:
    #       print(f"{e}")

# Добавление товара
#     try:
#         Motorola = store.find_manufacturer_by_id(2)
#         if not Motorola:
#             all_manuf = store.get_all_manufacturer()
#             Motorola = next((m for m in all_manuf if "Motorola" in m.name), None)
#
#         if Motorola:
#             phone = store.add_product(
#                 name="3310",
#                 manufacturer_id=Motorola.id,
#                 category="Смартфон",
#                 price=50000,
#                 serial_number="SN-NK-002578"
#             )
#             print(f"Товар добавлен {phone}")
#         else:
#             print("Производитель не найден")
#     except Exception as e:
#         print(f"ERROR {e}")

# Удаление товара
    store.delete_product(1)


if __name__ == "__main__":
    main()
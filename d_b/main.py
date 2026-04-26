from models import StoreManager

def main():
    print("Start")
    store_manager = StoreManager("database.db")

    print("Create manufacturer")
    sony = store_manager.add_manufacturer("Sony")
    print(sony)

if __name__ == "__main__":
    main()
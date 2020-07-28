
# Wykorzystaj csv.writer i zapisz stan magazynu przed wyłączeniem programu do pliku csv -
# tego samego, z którego zostanie wczytany po kolejnym uruchomieniu.

from shop import user_interface
from shop.persistence import load_store, save_store
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)


if __name__ == '__main__':
    run_homework()

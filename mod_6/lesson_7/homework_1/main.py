
# Utwórz “ręcznie” plik csv zawierający informacje o dostępnych produktach.
# Wykorzystaj csv.reader i napisz funkcję “ładującą” stan magazynu z pliku csv.
# Uruchamiaj ją za każdym razem przy starcie programu.

from shop import user_interface
from shop.persistence import load_store
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()


if __name__ == '__main__':
    run_homework()

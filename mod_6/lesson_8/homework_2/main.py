
# Dodaj możliwość wyświetlenia historii zamówień na podstawie imienia i nazwiska klienta.
# Odszukaj odpowiednie zamówienia w pliku orders.json i wypisz dane o nich użytkownikowi.
# W razie potrzeby zmodyfikuj strukturę w pliku orders.json.

from shop import user_interface
from shop.persistence import load_store, save_store
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)


if __name__ == "__main__":
    run_homework()

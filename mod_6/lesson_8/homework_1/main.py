
# Zapisz informację o zamówieniu w pliku orders.json. Na liście zamówień
# (np. pod kluczem orders) powinny znajdować się wszystkie zrealizowane zamówienia.
# Przed każdym wyłączeniem programu aktualne zamówienie powinno zostać dodane do tej listy.
# Pomiń zapisywanie informacji o polityce rabatowej.
# Możesz również tymczasowo wyłączyć możliwość wypisywania historii zamówień
# zaimplementowaną wcześniej w oparciu o plik orders.txt

from shop import user_interface
from shop.persistence import load_store, save_store
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)


if __name__ == "__main__":
    run_homework()


# Zastąp implementację wczytywania i zapisywania wykorzystującą csv.reader i csv.writer taką,
# która użyje csv.DictReader i csv.DictWriter.

from shop import user_interface
from shop.persistence import load_store, save_store
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)


if __name__ == '__main__':
    run_homework()

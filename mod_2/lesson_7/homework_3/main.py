
# Utwórz klasę TaxCalculator z metodą statyczną obliczającą podatek dla danej pozycji z zamówieniu.
# Przyjmij następujące stawki podatkowe - w zależności od nazwy kategorii, w do której należy produkt:
# 5% - “Owoce i warzywa”
# 8% - “Jedzenie”
# 20% - Wszystkie pozostałe kategorie
from order_element import OrderElement
from shop.product import Product
from shop.tax_calculator import TaxCalculator


def run_homework():
    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    tomato = Product(name="Pomidor", category_name="Owoce i warzywa", unit_price=3)
    something = Product(name="Coś", category_name="Nieznana kategoria", unit_price=50)
    ten_cookies = OrderElement(cookie, quantity=10)
    five_tomatoes = OrderElement(tomato, quantity=5)
    single_something = OrderElement(something, quantity=1)

    cookies_tax = TaxCalculator.tax_for_order_element(ten_cookies)
    tomatoes_tax = TaxCalculator.tax_for_order_element(five_tomatoes)
    something_tax = TaxCalculator.tax_for_order_element(single_something)

    print(f"Cena ciastek: {ten_cookies.calculate_price()} + {cookies_tax:.2f}")
    print(f"Cena pomidorów: {five_tomatoes.calculate_price()} + {tomatoes_tax:.2f}")
    print(f"Cena czegoś: {single_something.calculate_price()} + {something_tax:.2f}")


if __name__ == '__main__':
    run_homework()


# Stwórz klasę reprezentującą produkt z terminem ważności (dziedziczącą po klasie Product).
# Rozszerz implementację bazową o dodatkowe pola rok produkcji oraz liczbę lat ważności i metodę does_expire,
# która przyjmuje jako argument aktualny rok i sprawdza czy od daty produkcji do podanego roku
# minęła liczba lat większa od podanej jako lata ważności.

from shop.product import ExpiringProduct


def run_homework():

    cookies = ExpiringProduct(
        name="Ciasteczka czekoladowe",
        category_name="Jedzenie",
        unit_price=4,
        production_year=2020,
        validity_years=2
    )
    print(cookies.does_expire(2020))
    print(cookies.does_expire(2023))


if __name__ == '__main__':
    run_homework()

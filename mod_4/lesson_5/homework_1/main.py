
# Rozbuduj rozwiązanie zadania drugiego z poprzedniej lekcji dodając funkcję, która będzie sprawdzać,
# których z zamówionych produktów jeszcze brakuje, po otrzymaniu kolejnej dostawy.
# W tym celu najpierw zaimplementuj funkcję, products_delivery, która reprezentuje otrzymanie dostawy produktów.
# Funkcja ta powinna zwracać listę produktów przywiezionych w ramach dostawy -
# w ramach symulacji niech wylosuje z powtórzeniami pięć nazw produktów
# (z listy dziesięciu dostępnych produktów wylosuj pięć elementów ale tak,
# żeby mogły się one powtórzyć na liście wynikowej).
# W skrypcie main najpierw “zamów dostawę”, a potem sprawdź, które produkty są jeszcze potrzebne.
# Aby porównać otrzymane produkty z listą jeszcze potrzebnych wykorzystaj set.
# Następnie tak długo realizuj kolejne zamówienia aż ostatecznie wszystkie z potrzebnych produktów zostaną dostarczone.
from shop.delivery import products_delivery


def run_homework():
    needed_products = [
        "chleb",
        "ciastka",
        "jabłka",
        "dżem",
        "pomarańcze",
        "marchew",
        "bułki",
        "ziemniaki",
        "ser",
        "mleko"
    ]
    received_products = []

    while not set(needed_products) == set(received_products):
        new_products = products_delivery()
        received_products += new_products
        print(f"Otrzymano: {new_products}")
        missing_products = set(needed_products).difference(received_products)
        print(f"Brakuje nam jeszcze: {missing_products}")

    print(f"Łącznie otrzymano: {received_products}")


if __name__ == '__main__':
    run_homework()


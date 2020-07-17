import random


def run_example():
    bob_favourite_flavours = {"Malinowy", "Truskawkowy", "Jagodowy"}
    alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy"}
    print(bob_favourite_flavours)
    print(alice_favourite_flavours)

    # Suma dwóch zbiorów - smaki które są ulubionymi Boba lub Alice
    all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
    print(all_flavours)

    # # Część wspólna - smaki, które lubi zarówno Bob jak i Alice
    # common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
    # print(common_flavours)

    # # Różnica - smaki, które lubi Bob ale nie Alice
    # only_bob_flavours = bob_favourite_flavours.difference(alice_favourite_flavours)
    # print(only_bob_flavours)

    # # Sprawdzenie czy jeden zbiór jest pozdbiorem drugiego
    # print(bob_favourite_flavours.issubset(all_flavours))

    # # Usunięcie duplikatów
    # numbers = [random.randint(0, 40) for _ in range(100)]
    # no_duplicates = set(numbers)
    # print(len(numbers))
    # print(len(no_duplicates))

    # # Sprawdzenie czy dana lista zawiera wszystkie podane elementy (nie ważne ile razy i w jakiej kolejności)
    # digits = set([number for number in range(10)])
    # print(f"Czy udało się wylosować wszystkie cyfry? {digits.issubset(no_duplicates)}")


if __name__ == '__main__':
    run_example()

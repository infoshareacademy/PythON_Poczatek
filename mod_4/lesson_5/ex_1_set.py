def run_example():
    # Set możemy stworzyć przekazując kolekcję jako argument do wbudowanego konstruktora - set
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    bob_favourite_flavours = set(flavours)
    # Preferowanym sposobem względem przekazania kolekcji bezpośredni jest użycie klamrowych nawiasów
    # alice_favourite_flavours = set(["Pistacjowy", "Truskawkowy", "Orzechowy"])
    alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy"}
    # print(bob_favourite_flavours)
    # print(alice_favourite_flavours)

    # Za pomocą nawiasów klamrowych nie stworzymy pustego zbioru gdyż ten zapis jest "zajęty" przez słownik
    # not_working_empty_set = {}
    # empty_set = set()
    # print(type(not_working_empty_set))
    # print(type(empty_set))

    # W zbiorze elementy będą występować tylko jeden raz
    # alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy", "Orzechowy", "Orzechowy"}
    # print(alice_favourite_flavours)

    # # Za pomocą metody add możemy dodać element do zbioru
    alice_favourite_flavours.add("Waniliowy")
    # print(alice_favourite_flavours)

    # remove usuwa element
    # alice_favourite_flavours.remove("Pistacjowy")
    # print(alice_favourite_flavours)

    # dicard działa analogicznie do remove przy czym nie rzuca błędu gdy elementu nie ma w zbiorze
    # alice_favourite_flavours.discard("Pistacjowy")
    # print(alice_favourite_flavours)

    # pop wyciąga (usuwa i zwraca) element (nie wiadomo, który to będzie)
    # print(alice_favourite_flavours.pop())
    # print(alice_favourite_flavours)

    # # copy kopiuje zbiór, a clear usuwa wszystkie elementy
    # copy_of_flavours = alice_favourite_flavours.copy()
    # alice_favourite_flavours.clear()
    # print(alice_favourite_flavours)
    # print(copy_of_flavours)

    # Metoda update dodaje elementy z jednego zbioru do drugiego
    # all_flavours = alice_favourite_flavours.copy()
    # all_flavours.update(bob_favourite_flavours)
    # print(all_flavours)

    # # Długość zbioru to liczba jego elementów - tak jak w przypadku listy
    # print(len(bob_favourite_flavours))

    # # set nie pozwala na odwołania za pomocą indeksu - elementy nie mają kolejności
    # print(bob_favourite_flavours[0])

    # # Elementy zbioru muszą być hashable - nie możemy zagnieździć jednego setu w drugim
    # set_of_set = {{"Słony karmel", "Mango"}, {"Truskawkowy", "Śmietankowy"}}
    # print(set_of_set)


if __name__ == '__main__':
    run_example()

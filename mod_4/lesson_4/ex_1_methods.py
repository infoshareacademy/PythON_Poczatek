

def run_example():
    # W przykładach ze słownikiem posłużymy się słownikiem wydatków
    expenditures = {
        "prąd": [250],
        "woda": [30.45],
        "zakupy": [
            120.15,
            170.53,
            20.15
        ]
    }
    print(expenditures)

    # Metoda clear usuwa wszystkie elementy ze słownika
    # expenditures.clear()
    # print(expenditures)

    # Metoda copy tworzy i zwraca kopię słownika
    # expenditures_copy = expenditures.copy()
    # expenditures.clear()
    # print(expenditures)
    # print(expenditures_copy)

    # Za pomocą metody get możemy otrzymać wartość, która jest pod danym kluczem
    # Nie powoduje to "wyjęcia" elementu ze słownika - dalej tam jest
    # water_expenditures = expenditures.get("woda")
    # print(water_expenditures)
    # print(expenditures)

    # Get w przeciwieństwie do odwołania bezpośrednio po kluczu nie zwraca błędu tylko None gdy nie znajdzie klucza
    # cookies_expenditures = expenditures.get("ciasteczka")
    # # cookies_expenditures = expenditures["ciasteczka"]
    # print(cookies_expenditures)

    # Drugi, opcjonalny argument pozwala podać wartość, która zostanie zwrócona gdy dany klucz nie występuje w słowniku
    # cookies_expenditures = expenditures.get("ciasteczka", [10])
    # print(cookies_expenditures)

    # Za pomocą metody update możemy zaktualizować słownik o nowe klucze.
    # Nazwa argumentu zostanie użyta jako klucz
    # expenditures.update(jedzenie=[120], rozrywka=[70])
    # print(expenditures)

    # Jeżeli klucz się powtarza zostanie on nadpisany
    # expenditures.update(woda=[95])
    # print(expenditures)

    # Do metody update można też przekazać inny słownik
    # other_expenditures = {
    #     "remont": [1450],
    #     "internet": [40]
    # }
    # expenditures.update(other_expenditures)
    # print(expenditures)


if __name__ == '__main__':
    run_example()

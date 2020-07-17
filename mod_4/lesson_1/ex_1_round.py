import math


def run_example():
    # Zaokrąglanie za pomocą wbudowanej funkcji round - do najbliższej liczby całkowitej
    print(round(2.7))

    # Jeżeli dwie liczby są równie blisko to zaokrągla do parzystej
    print(round(1.5))
    print(round(2.5))

    # Opcjonalny argument ngdigits pozwala podać do jakiego miejsca zaokrąglamy
    print(round(3.129, ndigits=2))

    # Funkcja floor zwraca największą liczbę całkowitą, która jest mniejsza od podanej (podłoga)
    # print(math.floor(3.9))
    # print(math.floor(1.1))
    # print(math.floor(-1.1))

    # Funkcja ceil zwraca najmniejszą liczbę całkowitą, która jest większa od podanej (sufit)
    # print(math.ceil(3.9))
    # print(math.ceil(1.1))
    # print(math.ceil(-1.1))

    # Rzutowanie na int w ogólności działa analogicznie do math.floor.
    # W obu przypadkach ze względu na zmiennoprzecinkowy sposób reprezentacji floatów przy bardzo
    # "bliskich" wartościach zaokrąglenie nie zadziała poprawnie. Wynika to z tego, jak "pod spodem"
    # reprezentowany jest typ float. Jeżeli w naszych obliczeniach potrzebujemy dużej precyzji
    # to powinniśmy użyć np. typu Decimal
    # print(int(1.1))
    # print(int(1.9999))
    # print(int(1.9999999999999999999999999999))
    # print(math.floor(1.9999999999999999999999999999))


if __name__ == '__main__':
    run_example()

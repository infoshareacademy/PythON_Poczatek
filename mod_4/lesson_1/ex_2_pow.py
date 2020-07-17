import math


def run_example():
    # Najprostszym sposobem na podniesienie liczby do potęgi jest użycie operatora
    print(2 ** 5)

    # Funkcja wbudowana pow działa analogicznie
    print(pow(2, 10))

    # Jej dodatkowy argument pozwala na zwrócenie wartości modulo z potęgowania
    print(pow(2, 10, mod=10))

    # Funkcja pow z modułu math działa analogicznie, przy czym zawsze zamienie wartości na float
    print(math.pow(2, 8))


if __name__ == '__main__':
    run_example()

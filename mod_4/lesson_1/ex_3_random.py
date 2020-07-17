import random


def run_example():
    # Funkcja randint losuję liczbę całkowitą z podanego przedziału
    # W rzeczywistości liczby generowane przez random są pseudolosowe
    print(random.randint(5, 10))

    # uniform działa analogicznie dla wartości float
    print(random.uniform(-10, 20))


if __name__ == '__main__':
    run_example()

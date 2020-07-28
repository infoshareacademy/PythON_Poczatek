
def handle_even_number(number):
    try:
        if number % 2 != 0:
            raise ValueError("To nie jest liczba parzysta!")
    except TypeError as error:
        print("Zalogowano błąd związany z typem...")
        raise error

    print(f"Dzięki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number = input("Podaj liczbę parzystą: ")
    if number.isnumeric():
        number = int(number)

    try:
        handle_even_number(number)
    except TypeError as error:
        print(f"Coś nie tak z typem: {error}")
    except ValueError as error:
        print(f"Zła wartość: {error}")



if __name__ == '__main__':
    run_example()

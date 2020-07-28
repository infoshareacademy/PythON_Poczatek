
class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest poprawną liczbą")

    if number % 2 != 0:
        raise NumberParsingError("To nie jest liczba parzysta!")

    return number / 2


def run_example():
    number_str = input("Podaj liczbę parzystą: ")

    try:
        parsed_number = handle_even_number(number_str)
    except NumberParsingError as error:
        print(error)
    else:
        result = 100 / parsed_number
        print(f"Wynik magicznego działania to {result}")
    finally:
        print("Kończymy program...")


if __name__ == '__main__':
    run_example()

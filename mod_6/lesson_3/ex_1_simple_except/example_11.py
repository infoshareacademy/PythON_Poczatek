
class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest poprawną liczbą")

    if number % 2 != 0:
        raise NumberParsingError("To nie jest liczba parzysta!")

    print(f"Dzięki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number_str = input("Podaj liczbę parzystą: ")

    # try:
    #     handle_even_number(number_str)
    # except:
    #     print("Łapiemy absolutnie wszystko...")

    # try:
    #     handle_even_number(number_str)
    # except Exception:
    #     print("Łapiemy wszystko...")

    try:
        handle_even_number(number_str)
    except Exception as error:
        print(f"Tutaj też łapiemy wszystko ale przynajmniej coś z tym robimy: {error}")


if __name__ == '__main__':
    run_example()

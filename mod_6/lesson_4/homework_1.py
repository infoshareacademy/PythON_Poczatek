
# Napisz funkcję która zapyta użytkownika o pierwsze trzy litery imienia.
# Jeżeli wprowadzone zostanie mniej lub więcej liter to powinna rzucić wyjątek.
# Wywołaj funkcje wewnątrz bloku try i skorzystaj z sekcji except, else oraz finally wypisując różne komunikaty.


def ask_for_name():
    name = input("Podaj pierwsze trzy litery swojego imienia: ")
    name_len = len(name)
    if name_len < 3:
        raise ValueError("Za krótkie!")

    if name_len > 3:
        raise ValueError("Za długie!")

    print("Dziąkuję :) Ja jestem Python - następca języka ABC")


def run_homework():
    try:
        ask_for_name()
    except ValueError as error:
        print(f"Wprowadzono złe dane: {error}")
    else:
        print("Wszystko w porządku, możemy kontynuować")
    finally:
        print("Niezależnie od wszystkiego jesteś spoko!")


if __name__ == '__main__':
    run_homework()

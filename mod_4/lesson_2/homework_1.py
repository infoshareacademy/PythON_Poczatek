
#  Napisz funkcję która wczyta od użytkownika jej/jego imię i nazwisko,
#  “wyczyści je” z białych znaków na początku i końcu tekstu,
#  a następnie wypisze jakieś zdanie z tymi danymi
#  (np. “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)”


def run_example():
    first_name = input("Jak masz na imię? ")
    last_name = input("Jak brzmi Twoje nazwisko? ")
    first_name = first_name.strip()
    last_name = last_name.strip()

    print(f"Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)")


if __name__ == '__main__':
    run_example()


#  Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać metodę format


def run_example():
    first_name = input("Jak masz na imię? ")
    last_name = input("Jak brzmi Twoje nazwisko? ")
    first_name = first_name.strip()
    last_name = last_name.strip()

    print("Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)".format(
        first_name=first_name, last_name=last_name
    ))

    # print("Nazywasz się {} {} - jak miło Cię poznać :)".format(first_name, last_name))


if __name__ == '__main__':
    run_example()

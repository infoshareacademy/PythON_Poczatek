
#  Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać formatowanie z procentem


def run_example():
    first_name = input("Jak masz na imię? ")
    last_name = input("Jak brzmi Twoje nazwisko? ")
    first_name = first_name.strip()
    last_name = last_name.strip()

    print("Nazywasz się %(first_name)s %(last_name)s - jak miło Cię poznać :)" %
          {"first_name": first_name, "last_name": last_name})

    # print("Nazywasz się %s %s - jak miło Cię poznać :)" % (first_name, last_name))


if __name__ == '__main__':
    run_example()

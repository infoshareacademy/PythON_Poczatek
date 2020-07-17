
#  Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
#  Sprawdź, czy znajduje się wśród nich niebieski i wypisz odpowiedni komunikat


def run_example():
    favourite_colors = input("Jakie są Twoje ulubione kolory? Podaj wszystkie rozdzielając je przecinkiem: ")

    if favourite_colors.lower().find("niebieski") != -1:
        print("Lubisz niebieski!")
    else:
        print("Nie lubisz niebieskiego")

    # if "niebieski" in favourite_colors.lower():
    #     print("Lubisz niebieski!")
    # else:
    #     print("Nie lubisz niebieskiego")


if __name__ == '__main__':
    run_example()

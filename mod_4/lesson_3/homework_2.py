
# Wczytaj od użytkownika listę ulubionych sportów, a następnie stosując slicing wypisz co drugi pomijając pierwszy


def run_example():
    print("Jakie są Twoje ulubione sporty?")

    favourite_sports = []
    while True:
        sport = input("Podaj kolejny lub zakończ wpisując 'X': ")
        if sport == "X":
            break
        favourite_sports.append(sport)

    print(favourite_sports[1::2])


if __name__ == '__main__':
    run_example()

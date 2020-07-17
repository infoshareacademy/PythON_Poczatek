

def run_example():
    # W przykładzie wykorzystamy listę ulubionych smaków ;)
    favourite_flavours = [
        "malinowy",
        "truskawkowy",
        "czekoladowy",
        "pistacjowy",
        "kokosowy",
    ]
    print(favourite_flavours)

    # Metoda clear usuwa wszystkie elementy z listy
    # favourite_flavours.clear()
    # print(favourite_flavours)

    # Metoda reverse odwraca kolejność elementów na liście
    # favourite_flavours.reverse()
    # print(favourite_flavours)

    # Metoda count liczy liczbę wystąpień (analogicznie jak na str)
    # print(favourite_flavours.count("malinowy"))

    # Metoda copy tworzy kopię listy
    # copy_of_flavours = favourite_flavours.copy()
    # print(copy_of_flavours)

    # Metoda extend łączy dwie listy
    # new_flavours = ["orzechowy", "jagodowy"]
    # favourite_flavours.extend(new_flavours)
    # print(favourite_flavours)

    # Operator += działa tak samo
    # new_flavours = ["orzechowy", "jagodowy"]
    # favourite_flavours += new_flavours
    # print(favourite_flavours)

    # Operator * pozwala powtórzyć listę kilkukrotnie
    new_flavours = ["orzechowy", "jagodowy"] * 4
    print(new_flavours)




if __name__ == '__main__':
    run_example()


def run_example():
    # # Krotkę tworzymy za pomocą przecinka - rozdzielając nim kolejne elementy
    # human_info = "Bob", "Kowalski", 35
    # print(human_info)
    # print(type(human_info))

    # Nawiasy są opcjonalne - warto dodwać je tworząc wprost zmienną tuple dla zwiększenia czytelności
    human_info = ("Bob", "Kowalski", 35)
    # print(human_info)

    # # Do poszczególnych elementów krotki odwołujemy się za pomocą indeksu
    # print(human_info[0])
    # print(human_info[1])
    # print(human_info[2])
    # print(len(human_info))
    # # print(human_info[3])

    # Krotka jest immutable
    # human_info[0] = "Robert"
    # human_info.append(175)
    # human_info.sort()
    # del human_info[0]

    # # Krotka może mieć tylko jeden element
    # some_data = ("Mikołaj",)
    # print(some_data)

    # # Pustą krotkę tworzymy za pomocą nawiasów albo tuple
    # empty_tuple = ()
    # print(empty_tuple)
    # empty_tuple = tuple()
    # print(empty_tuple)

    # # Za pomocą tuple możemy też zamienić np. listę na krotkę
    numbers = [0, 1, 2, 3]
    tuple_numbers = tuple(numbers)
    print(tuple_numbers)

    # Po krotce możemy iterować
    for number in tuple_numbers:
        print(number)

if __name__ == '__main__':
    run_example()

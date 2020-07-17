

def run_example():
    # W przykładzie ze slicingiem najwygodniej będzie nam użyć listy z elementami o wartościach kolejnych indeksów
    numbers = []
    for number in range(15):
        numbers.append(number)
    print(numbers)

    # Podając pojedynczą wartość możemy uciąć listę z jednej lub drugiej strony - co poznaliśmy już wcześniej
    # print(numbers[:4])
    # print(numbers[8:])

    # Ponieważ slicing zawsze zwraca nową listę, nie podając żadnej liczby możemy uzyskać pełną kopię
    # copy_of_numbers = numbers[:]
    # print(copy_of_numbers)

    # Podając dwie wartości wycinamy listę z podanego przedziału
    # print(numbers[4:10])

    # Możemy podać również trzecią wartość, która oznacza co który element chcemy wybrać
    # W tym przypadku co trzeci element pomiędzy czwartym indeksem (włącznie) a 14 (bez 14)
    # print(numbers[4:14:3])

    # Powyższe możemy również zastosować dla ujemnych indeksów, jednak taki zapis jest już doś skomplikowany
    # print(numbers[2:-4:3])

    # Jeżeli pominiemy liczbę to będzie wykorzystana wartość domyślna (start = 0, koniec = długość, skok = 1)
    # print(numbers[2::3])


if __name__ == '__main__':
    run_example()

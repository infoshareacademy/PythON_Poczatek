
# Używając list comprehensions wygeneruj listy zawierające liczby od 1 do 30 podzielne kolejno przez 3 oraz przez 5
# (tzn. na pierwszej liście umieść liczby od 1 do 30 podzielne przez 3
# a na drugiej liczby od 1 do 30 podzielne przez 5). Połącz obie listy w jedną i wypisz wynik


def run_example():
    multiple_of_three = [number for number in range(1, 31) if number % 3 == 0]
    multiple_of_five = [number for number in range(1, 31) if number % 5 == 0]

    result = multiple_of_three + multiple_of_five
    print(result)


if __name__ == '__main__':
    run_example()

class ToBeFormatted:
    def __init__(self):
        pass

    def some_method(self):
        pass


def some_func(
    long_name_argument_1, long_name_argument_2, long_name_argument_3, long_name_argument_4,
):
    print("Hello!")


def run_example():
    print("Przykład formatowania")

    number = int(input("Podaj liczbę: "))

    if number > 10:
        if (number > 100 and number < 150) or (
            number > 10 and number < 100 and number % 2 == 0 or number % 3 == 0
        ):
            some_data = {
                1: "1",
                2: "2",
                3: "Ta liczba z jakiegoś powodu jest ważna i ma bardziej rozbudowany tekst niż inne",
                4: "4",
            }


if __name__ == "__main__":
    run_example()

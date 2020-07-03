
# Napisz funkcję która przyjmie dowolną liczbę argumentów pozycyjnych i zwróci napis
# powstały z połączenia ich z wykorzystaniem myślnika jako łącznika pomiędzy poszczególnymi argumentami


def combine_into_str(*args):
    result = ""
    for argument in args:
        result += str(argument)
        result += "-"
    # return "-".join(args)
    return result[:-1]


def run_homework():
    result = combine_into_str(1, 3, "Hello", 5, 2, "World")
    # result = combine_into_str("1", "3", "Hello", "5", "2", "World")
    print(result)


if __name__ == '__main__':
    run_homework()


def run_example():

    try:
        print("Przed rzuceniem wyjątku")
        raise TypeError("Coś poszło nie tak...")
        print("To się nie wydarzy")
    except ValueError as error:
        print("Wyjątek nie zostanie złapany, bo nie pasuje jego typ")

    print("I program będzie przetwarzany dalej :)")


if __name__ == '__main__':
    run_example()

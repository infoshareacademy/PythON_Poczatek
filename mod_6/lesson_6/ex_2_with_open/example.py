
def process_text_file():
    with open("plain_text.txt", mode="r") as plain_text_file:
        text_data = plain_text_file.read()

    print("Dane z pliku:")
    print(text_data)


def run_example():
    try:
        process_text_file()
    except IOError:
        print("Nie udało się wczytać danych...")

    print("Do zobaczenia później!")


if __name__ == '__main__':
    run_example()

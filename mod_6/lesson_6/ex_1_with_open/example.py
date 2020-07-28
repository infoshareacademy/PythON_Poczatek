
def run_example():
    path_to_file = "plain_text.txt"

    try:
        with open(path_to_file, mode="r") as plain_text_file:
            text_data = plain_text_file.read()
    except IOError:
        print("Nie udało się wczytać danych...")
    else:
        print("Dane z pliku:")
        print(text_data)

    print("Do zobaczenia później!")


if __name__ == '__main__':
    run_example()

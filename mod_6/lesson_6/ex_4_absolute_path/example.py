import os


def process_text_file(file_path):
    with open(file_path, mode="r") as plain_text_file:
        text_data = plain_text_file.read()

    print("Dane z pliku:")
    print(text_data)


def run_example():
    absolute_path = "/Users/mikolevy/Documents/kursy/PythON-Pocztek/code/mod_6/lesson_6/ex_4_absolute_path/plain_text.txt"
    # absolute_path = "C:/mikolevy/Documents/kursy/PythON-Pocztek/code/mod_6/lesson_6/ex_4_absolute_path/plain_text.txt"
    absolute_path = os.path.normpath(absolute_path)

    try:
        process_text_file(absolute_path)
    except IOError:
        print("Nie udało się wczytać danych...")

    print("Do zobaczenia później!")


if __name__ == '__main__':
    run_example()

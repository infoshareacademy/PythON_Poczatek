import os


def process_text_file(file_path):
    with open(file_path, mode="r") as plain_text_file:
        text_data = plain_text_file.read()

    print("Dane z pliku:")
    print(text_data)


def run_example():
    local_path = "plain_text.txt"
    # path_in_dir = "some_directory/other_file.txt"
    # path_in_dir_windows = "some_directory\\other_file.txt"
    path_in_dir = os.path.join("some_directory", "other_file.txt")

    try:
        process_text_file(local_path)
        # process_text_file(path_in_dir)
    except IOError:
        print("Nie udało się wczytać danych...")

    print("Do zobaczenia później!")


if __name__ == '__main__':
    run_example()

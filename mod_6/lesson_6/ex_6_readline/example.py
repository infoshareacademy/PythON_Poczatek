
def run_example():
    with open("plain_text.txt", mode="r") as plain_text_file:
        line = plain_text_file.readline()
        while line:
            print(f"Kolejna linia tekstu: {line}")
            line = plain_text_file.readline()


if __name__ == '__main__':
    run_example()

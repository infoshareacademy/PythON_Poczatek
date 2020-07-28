
def run_example():
    with open("plain_text.txt", mode="r") as plain_text_file:
        for line_number, line in enumerate(plain_text_file):
            print(f"{line_number}) {line}")


if __name__ == '__main__':
    run_example()

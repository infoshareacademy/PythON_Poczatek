
def run_example():
    print("Hello!")
    raise Exception("To jest błąd!")
    print("To już się nie wypisze...")


if __name__ == '__main__':
    run_example()

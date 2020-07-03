
def print_grades(**kwargs):
    # print(type(kwargs))
    for subject, grade in kwargs.items():
        print(f"Z przedmiotu: {subject} wystawiono: {grade}")


def run_example():
    print_grades(
        matematyka=4,
        fizyka=4,
        chemia=5,
        polski=4,
        biologia=4,
        geografia=3
    )

    # print("Pojedyncza wartość")
    # print("Jedna", "i druga")
    # print("Jedna", "i druga", "a nawet trzecia")

if __name__ == '__main__':
    run_example()
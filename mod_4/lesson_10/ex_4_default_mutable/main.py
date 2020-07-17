from estudent.subject import Subject


def run_example():
    math = Subject(identifier=1, name="Matematyka")
    print(math)

    math.assign_teacher("Bob")
    math.assign_teacher("Alice")
    print(math)


if __name__ == '__main__':
    run_example()

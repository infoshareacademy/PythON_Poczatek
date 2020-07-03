
def print_grades(**kwargs):
    for subject, grade in kwargs.items():
        print(f"Z przedmiotu: {subject} wystawiono: {grade}")


def run_example():
    grades = {
        "matematyka": 4,
        "fizyka": 4,
        "chemia": 5,
    }

    print_grades(grades)
    # print_grades(**grades)

    # more_grades = {
    #     "polski": 4,
    #     "biologia": 4,
    #     "geografia": 3
    # }
    #
    # all_grades = {**grades, **more_grades}
    # print(all_grades)


if __name__ == '__main__':
    run_example()
from estudent.school import create_school_with_students


def run_example():
    school = create_school_with_students("Hogwart")
    school.print_self()


if __name__ == '__main__':
    run_example()

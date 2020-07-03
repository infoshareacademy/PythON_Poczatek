from estudent.school import School


def run_example():
    school = School.create_school_with_students("Hogwart")
    print(school)

    print(f"W szkole może być maksymalnie {school.MAX_STUDENTS_NUMBER} uczniów")


if __name__ == '__main__':
    run_example()

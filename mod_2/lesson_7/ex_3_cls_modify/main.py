from estudent.school import School


def run_example():
    school = School.create_school_with_students("Hogwart")
    new_school = School.create_school_with_students("New School")

    print("school.MAX_STUDENTS_NUMBER:", school.MAX_STUDENTS_NUMBER)
    print("new_school.MAX_STUDENTS_NUMBER:", new_school.MAX_STUDENTS_NUMBER)

    print()
    print("Po modyfikacji na poziomie obiektu")
    school.MAX_STUDENTS_NUMBER = 125
    print("school.MAX_STUDENTS_NUMBER:", school.MAX_STUDENTS_NUMBER)
    print("new_school.MAX_STUDENTS_NUMBER:", new_school.MAX_STUDENTS_NUMBER)

    print()
    print("school self:")
    school.self_print_max_student_number()
    print("school cls:")
    school.cls_print_max_student_number()

    print()
    print("Po modyfikacji na poziomie klasy")
    School.MAX_STUDENTS_NUMBER = 330
    print("school.MAX_STUDENTS_NUMBER:", school.MAX_STUDENTS_NUMBER)
    print("new_school.MAX_STUDENTS_NUMBER:", new_school.MAX_STUDENTS_NUMBER)
    print("school self:")
    school.self_print_max_student_number()
    print("school cls:")
    school.cls_print_max_student_number()
    another_school = School.create_school_with_students("Other")
    print("another_school.MAX_STUDENTS_NUMBER:", another_school.MAX_STUDENTS_NUMBER)


if __name__ == '__main__':
    run_example()

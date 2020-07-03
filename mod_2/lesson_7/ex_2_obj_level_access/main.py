from estudent.school import School
from estudent.student import Student


def run_example():
    school = School.create_school_with_students("Hogwart")
    harry = Student(first_name="Harry", last_name="Potter")
    school.assign_student(harry)
    print(school)

    new_school = school.create_school_with_students("New School")

    print(school.MAX_STUDENTS_NUMBER)
    print(new_school.MAX_STUDENTS_NUMBER)


if __name__ == '__main__':
    run_example()

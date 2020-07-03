
from estudent.school import create_school_with_students


def run_example():
    school = create_school_with_students("Hogwart")
    student = school.students[0]
    student.add_final_grade(5)

    print(student.__final_grades)
    school.__promote_lucky_students()


if __name__ == '__main__':
    run_example()

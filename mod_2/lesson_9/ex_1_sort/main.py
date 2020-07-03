from estudent.school import School


def run_example():
    school = School.create_school_with_students("Hogwart")
    students = school.students
    for student in students:
        print(student)
    print("-" * 20)

    students.sort(key=lambda student: student.grades_avg())

    for student in students:
        print(student)


if __name__ == '__main__':
    run_example()

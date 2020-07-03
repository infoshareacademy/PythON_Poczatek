import random

from estudent.school import create_school_with_students


def final_grades_no_encapsulation(school):
    for student in school.students:
        final_grade = random.randint(1, 3)
        student.final_grades.append(final_grade)
    print(school)


def final_grades_with_encapsulation(school):
    for student in school.students:
        final_grade = random.randint(1, 3)
        student.add_final_grade(final_grade)
    print(school)


def run_example():
    school = create_school_with_students("Hogwart")

    for student in school.students:
        student.promote()
    # print(school)
    # print("=" * 20)

    final_grades_no_encapsulation(school)
    print("=" * 20)
    final_grades_with_encapsulation(school)


if __name__ == '__main__':
    run_example()

from estudent.grade_calculator import GradeCalculator
from estudent.school import School


def grades_avg_for_student(student):
    return student.grades_avg()


def run_example():
    school = School.create_school_with_students("Hogwart")
    students = school.students

    for student in students:
        # student.add_final_grade(1)
        student.add_final_grade(1, check_promotion_policy=GradeCalculator.strict_promotion_policy)

    students.sort(key=grades_avg_for_student, reverse=True)
    for student in students:
        print(student)


if __name__ == '__main__':
    run_example()

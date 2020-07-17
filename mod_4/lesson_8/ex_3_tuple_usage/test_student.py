from estudent.grade_calculator import GradeCalculator
from estudent.student import Student


def test_add_final_grades():
    parameters = [
        (5, "Matematyka", None, True),
        (5, "Historia", None, True),
        (1, "Matematyka", None, True),
        (5, "Matematyka", GradeCalculator.normal_promotion_policy, True),
        (2, "Matematyka", GradeCalculator.strict_promotion_policy, False),
    ]

    for params in parameters:
        grade, subject, promotion_policy, promoted = params
        student = Student("Bob", "Kowalski")
        student.add_final_grade(grade, subject, promotion_policy)

        if student.promoted == promoted:
            print("OK")
        else:
            print(f"Błąd! Dla parametrów: {params} wynik promocji to {student.promoted} zamiast {promoted}")


def run_test():
    test_add_final_grades()


if __name__ == '__main__':
    run_test()
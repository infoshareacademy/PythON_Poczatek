from estudent.grade import Grade, FinalGrade
from estudent.subject import Subject


def run_example():
    best_grade = Grade(value=6)
    failing_grade = Grade(value=1)
    print(best_grade)
    print(failing_grade)
    print(best_grade.is_passing())
    print(failing_grade.is_passing())

    # no_value_grade = Grade()

    # math = Subject(identifier=1, name="Matematyka")
    # print(math)


if __name__ == '__main__':
    run_example()

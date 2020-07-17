
from estudent.grade import Grade


def run_example():
    best_grade = Grade(value=6)
    print(best_grade)
    best_grade.value = 1
    print(best_grade.is_passing())


if __name__ == '__main__':
    run_example()

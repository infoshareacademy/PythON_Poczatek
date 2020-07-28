
from estudent.persistence import load_students_from_csv


def run_example():
    for student in load_students_from_csv():
        print(student)


if __name__ == '__main__':
    run_example()

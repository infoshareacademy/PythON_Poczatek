from estudent import data_generator
from estudent.persistence import save_students_as_csv


def run_example():
    students = data_generator.generate_students(number_of_students=10)
    save_students_as_csv(students)


if __name__ == '__main__':
    run_example()

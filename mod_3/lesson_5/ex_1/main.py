from estudent import data_generator


def run_example():
    students = data_generator.generate_students()
    print(students.first_student)


if __name__ == '__main__':
    run_example()

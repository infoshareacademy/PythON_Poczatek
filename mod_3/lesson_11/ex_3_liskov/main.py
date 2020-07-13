from estudent.data_generator import StudentGenerator, StudentGoodGradesGenerator


def run_example():
    students_generators = [
        StudentGenerator(),
        StudentGoodGradesGenerator()
    ]

    for generator in students_generators:
        # generator.configure_grades(min_grade=4, max_grade=5)
        students = generator.generate_students()
        print(students)


if __name__ == '__main__':
    run_example()

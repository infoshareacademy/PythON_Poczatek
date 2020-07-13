
from estudent import data_generator
from estudent.school import School


def run_example():
    students = data_generator.generate_students()
    school = School(name="Hogwart", students=students)
    print(school)


if __name__ == '__main__':
    run_example()

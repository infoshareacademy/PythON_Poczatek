
from estudent import data_generator
from estudent.grade import Grade
from estudent.grade_calculator import GradeCalculator
from estudent.school import School
from estudent.student import Student


def run_example():
    students = data_generator.generate_students(number_of_students=45)
    school = School(name="Mała szkoła", students=[])
    school.students = students

    # school = School(name="Mała szkoła", students=data_generator.generate_students())


if __name__ == '__main__':
    run_example()

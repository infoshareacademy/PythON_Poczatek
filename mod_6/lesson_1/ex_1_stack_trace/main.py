import geopy

from estudent import data_generator
from estudent.student import Student


def run_example():
    # students = data_generator.generate_students()
    # print(students[145])

    # student = Student(first_name="Mikołaj", last_name="Lewandowski")
    # print(student.grades_avg)

    geo_locator = geopy.Nominatim()


if __name__ == '__main__':
    run_example()

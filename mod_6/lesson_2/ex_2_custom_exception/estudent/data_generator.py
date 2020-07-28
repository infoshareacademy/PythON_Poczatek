import random

from estudent.config import Config
from estudent.school import School
from estudent.student import Student


def generate_students(number_of_students=None):
    if number_of_students is None:
        number_of_students = random.randint(1, School.MAX_STUDENTS_NUMBER)

    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        student = Student(first_name, last_name)
        students.append(student)
        subjects = ["Matematyka", "Fizyka", "Biologia", "Chemia", "Historia"]
        for subject in subjects:
            final_grade = random.randint(Config.MIN_RANDOM_GRADE, Config.MAX_RANDOM_GRADE)
            student.add_final_grade(final_grade, subject)
    return students

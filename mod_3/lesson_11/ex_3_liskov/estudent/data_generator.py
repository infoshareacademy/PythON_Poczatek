import random

from estudent.config import Config
from estudent.school import School
from estudent.student import Student


class StudentGenerator:

    def __init__(self, number_of_students=None):
        if number_of_students is None:
            number_of_students = random.randint(1, School.MAX_STUDENTS_NUMBER)
        self.number_of_students = number_of_students

    def generate_students(self):
        students = []
        for student_number in range(self.number_of_students):
            first_name = f"Student-{student_number}"
            last_name = "Smith"
            student = Student(first_name, last_name)
            students.append(student)
            subjects = ["Matematyka", "Fizyka", "Biologia", "Chemia", "Historia"]
            for subject in subjects:
                final_grade = random.randint(Config.MIN_RANDOM_GRADE, Config.MAX_RANDOM_GRADE)
                student.add_final_grade(final_grade, subject)
        return students


class StudentGoodGradesGenerator(StudentGenerator):

    def __init__(self, number_of_students=None):
        super().__init__(number_of_students)
        self.min_grade = None
        self.max_grade = None

    def configure_grades(self, min_grade, max_grade):
        self.min_grade = min_grade
        self.max_grade = max_grade

    def generate_students(self):
        if self.min_grade is None or self.max_grade is None:
            return "ERROR"

        students = []
        for student_number in range(self.number_of_students):
            first_name = f"Student-{student_number}"
            last_name = "Smith"
            student = Student(first_name, last_name)
            students.append(student)
            subjects = ["Matematyka", "Fizyka", "Biologia", "Chemia", "Historia"]
            for subject in subjects:
                final_grade = random.randint(self.min_grade, self.max_grade)
                student.add_final_grade(final_grade, subject)
        return students

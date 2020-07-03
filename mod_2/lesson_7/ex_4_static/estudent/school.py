import random

from estudent.config import Config
from estudent.student import Student


class School:

    MAX_STUDENTS_NUMBER = 20

    def __init__(self, name, students):
        self.name = name
        self.students = students
        self._promote_lucky_students()

    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def __str__(self):
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"School: {self.name}, with {len(self.students)} students: {students}"

    @classmethod
    def create_school_with_students(cls, school_name):
        number_of_students = random.randint(1, cls.MAX_STUDENTS_NUMBER)
        school = School(school_name, students=[])

        for student_number in range(number_of_students):
            first_name = f"Student-{student_number}"
            last_name = "Smith"
            student = Student(first_name, last_name)
            school.assign_student(student)
            for _ in range(Config.RANDOM_FINAL_GRADES_NUMBER):
                final_grade = random.randint(Config.MIN_RANDOM_GRADE, Config.MAX_RANDOM_GRADE)
                student.add_final_grade(final_grade)

        return school

    def assign_student(self, student):
        if len(self.students) < School.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            print("Nie ma już miejsca!")

    def self_print_max_student_number(self):
        print(self.MAX_STUDENTS_NUMBER)

    @classmethod
    def cls_print_max_student_number(cls):
        print(cls.MAX_STUDENTS_NUMBER)

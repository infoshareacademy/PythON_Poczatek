from estudent.grade import Grade
from estudent.grade_calculator import GradeCalculator


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades = []

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}"

    def promote(self):
        self.promoted = True

    def add_final_grade(self, grade):
        self._final_grades.append(Grade(value=grade))
        if not self.check_promotion():
            self.promoted = False
        else:
            self.promoted = True

    def check_promotion(self):
        return GradeCalculator.check_student_promotion(self._final_grades)


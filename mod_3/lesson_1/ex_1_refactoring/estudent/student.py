from estudent.grade import Grade
from estudent.grade_calculator import GradeCalculator


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades = []

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promowany: {self.promoted}, średnia: {self.grades_avg():.2f}"

    def grades_avg(self):
        return GradeCalculator.calculate_student_avg(self._final_grades)

    def promote(self):
        self.promoted = True

    def add_final_grade(self, grade, check_promotion_policy=None):
        if check_promotion_policy is None:
            check_promotion_policy = GradeCalculator.normal_promotion_policy
        self._final_grades.append(Grade(value=grade))
        if check_promotion_policy(self._final_grades):
            self.promoted = True
        else:
            self.promoted = False

from estudent.grade import FinalGrade, Grade
from estudent.grade_calculator import GradeCalculator


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades = []

    @staticmethod
    def from_csv(first_name, last_name, promoted, grades_values):
        student = Student(first_name, last_name)
        student.promoted = promoted
        student._final_grades = [Grade(value=grade_value) for grade_value in grades_values]
        return student

    @staticmethod
    def from_json(first_name, last_name, promoted, final_grades):
        student = Student(first_name, last_name)
        student.promoted = promoted
        student._final_grades = [FinalGrade(**grade) for grade in final_grades]
        return student

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promowany: {self.promoted}, średnia: {self.grades_avg:.2f}"

    @property
    def final_grades(self):
        return self._final_grades

    def final_grade_from_subject(self, subject):
        for final_grade in self._final_grades:
            if final_grade.subject == subject:
                return final_grade

    @property
    def grades_avg(self):
        return GradeCalculator.calculate_student_avg(self._final_grades)

    def promote(self):
        self.promoted = True

    def add_final_grade(self, grade, subject, check_promotion_policy=None):
        if check_promotion_policy is None:
            check_promotion_policy = GradeCalculator.normal_promotion_policy
        self._final_grades.append(FinalGrade(value=grade, subject=subject))

        if check_promotion_policy(self._final_grades):
            self.promoted = True
        else:
            self.promoted = False

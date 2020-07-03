from estudent.grade import Grade


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.__final_grades = []

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}"

    def promote(self):
        self.promoted = True

    def add_final_grade(self, grade):
        self.__final_grades.append(Grade(value=grade))
        if grade == 1:
            self.promoted = False


class Department:

    def __init__(self, letter_identifier, year):
        self.letter_identifier = letter_identifier
        self.year = year
        self.students = []

    def assign_student(self, student):
        self.students.append(student)
        return True

    def __str__(self):
        return f"Klasa {self.year}{self.letter_identifier}, {len(self.students)} uczniów"


class SizeLimitedDepartment(Department):

    MAX_STUDENTS = 15

    def assign_student(self, student):
        if len(self.students) < SizeLimitedDepartment.MAX_STUDENTS:
            self.students.append(student)
            return True
        else:
            print("Nie ma już miejsca")
            return False

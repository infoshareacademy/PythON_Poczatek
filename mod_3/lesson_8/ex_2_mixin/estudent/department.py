import random


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


class RemoteDepartment(Department):

    def generate_online_id_for_students(self):
        for student in self.students:
            identifier = random.randint(1, 1000)
            print(f"Identyfikator dla studenta {student}: {identifier}")


class BioChemRemoteSizeLimitDepartment(RemoteDepartment, SizeLimitedDepartment):
    MIN_BIO_GRADE = 3
    MIN_CHEM_GRADE = 3

    def assign_student(self, student):
        bio_grade = student.final_grade_from_subject("Biologia")
        chem_grade = student.final_grade_from_subject("Chemia")
        if bio_grade.value >= self.MIN_BIO_GRADE and chem_grade.value >= self.MIN_CHEM_GRADE:
            return super().assign_student(student)
        else:
            print("Za słabe oceny :-/")
            return False


class GeneralRemoteSizeLimitDepartment(RemoteDepartment, SizeLimitedDepartment):
    pass


class GeneralRemoteDepartment(RemoteDepartment):
    pass


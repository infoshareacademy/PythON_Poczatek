
class Department:

    MAX_STUDENTS = 20

    def __init__(self, letter_identifier, year):
        self.letter_identifier = letter_identifier
        self.year = year
        self.students = []

    def assign_student(self, student):
        if len(self.students) < Department.MAX_STUDENTS:
            self.students.append(student)
            return True
        else:
            print("Nie ma już miejsca")
            return False

    def __str__(self):
        return f"Klasa {self.year}{self.letter_identifier}, {len(self.students)} uczniów"


class BioChemDepartment(Department):
    MIN_BIO_GRADE = 3
    MIN_CHEM_GRADE = 3

    def assign_student(self, student):
        if len(self.students) < Department.MAX_STUDENTS:
            bio_grade = student.final_grade_from_subject("Biologia")
            chem_grade = student.final_grade_from_subject("Chemia")
            if bio_grade.value >= self.MIN_BIO_GRADE and chem_grade.value >= self.MIN_CHEM_GRADE:
                self.students.append(student)
                return True
            else:
                print("Za słabe oceny :-/")
                return False
        else:
            print("Nie ma już miejsca")
            return False


class MathPhysicsDepartment(Department):
    MIN_MATH_GRADE = 3
    MIN_PHYSICS_GRADE = 3

    def assign_student(self, student):
        if len(self.students) < Department.MAX_STUDENTS:
            math_grade = student.final_grade_from_subject("Matematyka")
            physics_grade = student.final_grade_from_subject("Fizyka")
            if math_grade.value >= self.MIN_MATH_GRADE and physics_grade.value >= self.MIN_PHYSICS_GRADE:
                self.students.append(student)
                return True
            else:
                print("Za słabe oceny :-/")
                return False
        else:
            print("Nie ma już miejsca")
            return False

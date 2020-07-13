
class School:

    MAX_STUDENTS_NUMBER = 20

    def __init__(self, name, students):
        self.name = name
        self._students = students
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

        return f"Szkoła: {self.name}, z {len(self.students)} uczniami: {students}"

    @property
    def students(self):
        return self._students

    @property
    def best_student(self):
        if len(self.students):
            return sorted(self.students, key=lambda student: student.grades_avg, reverse=True)[0]
        return None

    def assign_student(self, student):
        if len(self.students) < School.MAX_STUDENTS_NUMBER:
            self._students.append(student)
        else:
            print("Nie ma już miejsca!")

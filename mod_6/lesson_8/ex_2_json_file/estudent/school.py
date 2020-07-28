from estudent.errors import PlacesLimitError


class School:

    MAX_STUDENTS_NUMBER = 50
    MAX_STUDENTS_PER_DEPARTMENT = 15

    def __init__(self, name, students):
        self.name = name
        self._students = students
        self._promote_lucky_students()
        self.departments = self._split_students_to_departments()

    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def _split_students_to_departments(self):
        departments = {}
        departments_letters = ["A", "B", "C", "D", "E", "F"]
        places_in_departments = len(departments_letters) * School.MAX_STUDENTS_PER_DEPARTMENT
        if places_in_departments < len(self._students):
            raise PlacesLimitError(places_limit=School.MAX_STUDENTS_PER_DEPARTMENT)

        current_department_number = -1
        for index, student in enumerate(self.students):

            if index % School.MAX_STUDENTS_PER_DEPARTMENT == 0:
                current_department_number += 1

            current_department = departments_letters[current_department_number]
            if current_department not in departments:
                departments[current_department] = []

            departments[current_department].append(student)
        return departments

    def __str__(self):
        result = ""
        for department_name, students_in_department in self.departments.items():
            result += f"Oddział {department_name}\n"
            for student in students_in_department:
                result += f"{student}\n"

        return f"Szkoła: {self.name}, z {len(self.students)} uczniami: \n{result}"

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, value):
        if len(value) < School.MAX_STUDENTS_NUMBER:
            self._students = value
        else:
            raise PlacesLimitError(
                places_limit=School.MAX_STUDENTS_NUMBER,
                message=f"W szkole jest tylko {School.MAX_STUDENTS_NUMBER} miejsc,"
                        f" nie można przypisać {len(value)} uczniów"
            )
        self.departments = self._split_students_to_departments()

    @property
    def best_student(self):
        if len(self.students):
            return sorted(self.students, key=lambda student: student.grades_avg)
        return None

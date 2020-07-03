
class School:

    # Konstruktor z domyślnym argumentem - uwaga na domyślną listę!
    def __init__(self, name, students=None):
        self.name = name

        if students is None:
            students = []
        self.students = students


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


# Uwaga - ponownie side effect
def assign_student_to_school(school, student):
    school.students.append(student)


def run_example():
    school_without_students = School("Pusta szkoła")
    first_student = Student(first_name="Jakub", last_name="Kowalski")
    assign_student_to_school(school_without_students, first_student)

    for student in school_without_students.students:
        print_student(student)


if __name__ == '__main__':
    run_example()

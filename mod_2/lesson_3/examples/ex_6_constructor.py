
class School:

    # Konstruktor nie musi "wprost" przypisywać przekazanych wartości, może wykonać swoją logikę
    def __init__(self, name, students):
        self.name = name
        if len(students) > 10:
            students = students[:10]
        self.students = students


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


def create_school_with_students(school_name, number_of_students):
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():
    school = create_school_with_students("Hogwart", 40)
    print(school)
    for student in school.students:
        print_student(student)


if __name__ == '__main__':
    run_example()
import random


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __repr__(self):
        return f"<Student first_name='{self.first_name}', last_name='{self.last_name}', promoted={self.promoted}>"


class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __repr__(self):
        students_reprs = []
        for student in self.students:
            students_reprs.append(repr(student))
        all_students_repr = ", ".join(students_reprs)

        return f"<School name='{self.name}', students=[{all_students_repr}]>"


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():
    school = create_school_with_students("Hogwart")
    school_str = str(school)
    print(school_str)


if __name__ == '__main__':
    run_example()

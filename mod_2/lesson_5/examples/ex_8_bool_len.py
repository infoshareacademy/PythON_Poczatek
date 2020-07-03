import random


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students

    # def __len__(self):
    #     return len(self.students)


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
    school.students = []
    print(bool(school))


if __name__ == '__main__':
    run_example()

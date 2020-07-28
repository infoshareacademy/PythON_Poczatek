import random

from estudent.school import School
from estudent.student import Student

MIN_RANDOM_GRADE = 1
MAX_RANDOM_GRADE = 6

FEMALE_FIRST_NAMES = [
    "Ala",
    "Karolina",
    "Ola",
    "Ania",
]

MALE_FIRST_NAMES = [
    "Bob",
    "Mikołaj",
    "Kuba",
    "Emil"
]

FEMALE_LAST_NAMES = [
    "Kowalska",
    "Nowak",
    "Wiśniewska",
    "Kamińska",
    "Lewandowska",
    "Wójcik",
    "Szymańska",
]

MALE_LAST_NAMES = [
    "Kowalski",
    "Nowak",
    "Wiśniewski",
    "Kamiński",
    "Lewandowski",
    "Wójcik",
    "Szymański",
]


def generate_students(number_of_students=None):
    if number_of_students is None:
        number_of_students = random.randint(1, School.MAX_STUDENTS_NUMBER)

    students = []
    for student_number in range(number_of_students):
        first_name, last_name = generate_random_name()
        student = Student(first_name, last_name)
        students.append(student)
        subjects = ["Matematyka", "Fizyka", "Biologia", "Chemia", "Historia"]
        for subject in subjects:
            final_grade = random.randint(MIN_RANDOM_GRADE, MAX_RANDOM_GRADE)
            student.add_final_grade(final_grade, subject)
    return students


def generate_random_name():

    if random.randint(0, 1):
        first_name_index = random.randint(0, len(FEMALE_FIRST_NAMES) - 1)
        last_name_index = random.randint(0, len(FEMALE_LAST_NAMES) - 1)
        return FEMALE_FIRST_NAMES[first_name_index], FEMALE_LAST_NAMES[last_name_index]
    else:
        first_name_index = random.randint(0, len(MALE_FIRST_NAMES) - 1)
        last_name_index = random.randint(0, len(MALE_LAST_NAMES) - 1)
        return MALE_FIRST_NAMES[first_name_index], MALE_LAST_NAMES[last_name_index]

from estudent import data_generator
from estudent.persistence import StudentsCSVSerializer, StudentsCSVDictSerializer


def load_and_save_students(students_serializer):
    for student in students_serializer.load_students():
        print(student)

    print()
    print("Jeszcze raz ci sami uczniowie:")
    for cached_student in students_serializer.load_students():
        print(cached_student)

    new_students = data_generator.generate_students(number_of_students=10)
    students_serializer.save_students(new_students)


def run_example():
    # students_serializer = StudentsCSVSerializer()
    students_serializer = StudentsCSVDictSerializer()
    load_and_save_students(students_serializer)


if __name__ == '__main__':
    run_example()

import os

from estudent import data_generator


def run_example():
    students = data_generator.generate_students()

    # Ważna jest kolejność - najpierw with, a potem for inaczej będziemy ciągle otwierać i zamykać plik
    students_data_file_path = os.path.join("data", "students.txt")
    with open(students_data_file_path, mode="w") as students_file:
        for student in students:
            students_file.write(str(student))
            students_file.write("\n")

    new_students = data_generator.generate_students()
    with open(students_data_file_path, mode="a") as students_file:
        students_file.write("Dodatkowo dopisaliśmy jeszcze:\n")
        for student in new_students:
            students_file.write(str(student))
            students_file.write("\n")


if __name__ == "__main__":
    run_example()

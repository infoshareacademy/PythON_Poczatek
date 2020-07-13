from estudent import data_generator
from estudent.department import BioChemRemoteSizeLimitDepartment


def assign_students_to_department(department, students):
    not_qualified = []
    for student in students:
        if not department.assign_student(student):
            not_qualified.append(student)
    return not_qualified


def run_example():
    students_prefer_bio_chem = data_generator.generate_students(number_of_students=200)

    bio_chem_department = BioChemRemoteSizeLimitDepartment(letter_identifier="A", year=1)
    assign_students_to_department(bio_chem_department, students_prefer_bio_chem)

    print(bio_chem_department)
    bio_chem_department.generate_online_id_for_students()


if __name__ == '__main__':
    run_example()

from estudent import data_generator
from estudent.department import BioChemDepartment, MathPhysicsDepartment, Department


def assign_students_to_department(department, students):
    not_qualified = []
    for student in students:
        if not department.assign_student(student):
            not_qualified.append(student)
    return not_qualified


def run_example():
    students_prefer_bio_chem = data_generator.generate_students(number_of_students=10)
    students_prefer_math_physics = data_generator.generate_students(number_of_students=10)
    students = data_generator.generate_students(number_of_students=5)

    bio_chem_department = BioChemDepartment(letter_identifier="A", year=1)
    math_physics_department = MathPhysicsDepartment(letter_identifier="B", year=1)
    general_department = Department(letter_identifier="C", year=1)

    not_qualified_bio_chem = assign_students_to_department(bio_chem_department, students_prefer_bio_chem)
    not_qualified_math_physics = assign_students_to_department(math_physics_department, students_prefer_math_physics)
    not_qualified = assign_students_to_department(general_department, students)
    not_qualified += assign_students_to_department(general_department, not_qualified_bio_chem)
    not_qualified += assign_students_to_department(general_department, not_qualified_math_physics)

    print(bio_chem_department)
    print(math_physics_department)
    print(general_department)


if __name__ == '__main__':
    run_example()

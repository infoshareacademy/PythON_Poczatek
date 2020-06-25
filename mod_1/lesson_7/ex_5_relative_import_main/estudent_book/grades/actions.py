
from estudent_book.grades import promotion_status
from estudent_book.grades.grade_calculator import calculate_student_final_grades
from estudent_book.grades.promote import check_promotion
from estudent_book.students_data import is_student_in_school


def check_student_promotion():
    student_name = input("Podaj imię ucznia żeby dowiedzieć się czy zdał/zdała do następnej klasy: ")

    if not is_student_in_school(student_name):
        print(f"Niestety {student_name} nie ma na liście...")
    else:
        final_grades = calculate_student_final_grades(student_name)
        promotion_result = check_promotion(final_grades)

        if promotion_result == promotion_status.PASSED:
            print(f"Gratuluję! {student_name} zdał/zdała do następnej klasy :)")
        elif promotion_result == promotion_status.FAILED:
            print(f"Niestety {student_name} nie zdał/nie zdała")
        else:
            print("Coś poszło nie tak... Zgłoś to obsłudze systemu")

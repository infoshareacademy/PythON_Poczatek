
# Za pomocą import ... as możemy zaimportować moduł pod innną nazwą
from estudent.school import promotion_status as status
# import school.promotion_status as status
from estudent.school import calculate_student_final_grades
from estudent.school import check_promotion as promotion_checker
from estudent.school import is_student_in_school

print("Witaj w elektronicznym dzienniku!")

student_name = input("Podaj imię ucznia żeby dowiedzieć się czy zdał/zdała do następnej klasy: ")

if not is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma na liście...")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = promotion_checker(final_grades)

    if promotion_result == status.PASSED:
        print(f"Gratuluję! {student_name} zdał/zdała do następnej klasy :)")
    elif promotion_result == status.FAILED:
        print(f"Niestety {student_name} nie zdał/nie zdała")
    else:
        print("Coś poszło nie tak... Zgłoś to obsłudze systemu")


print(__name__)

from .students_data import find_student_by_name


def calculate_final_grade(all_grades):
    avg = sum(all_grades) / len(all_grades)
    final_grade = int(avg + 0.5)
    return final_grade


def calculate_student_final_grades(student_name):
    student = find_student_by_name(student_name)
    final_grades = {}
    for subject_result in student["subjects_results"]:
        subject_name = subject_result["subject"]
        final_grade = calculate_final_grade(subject_result["grades"])
        final_grades[subject_name] = final_grade
    return final_grades


from . import promotion_status

FAILED_GRADE = 1


def check_promotion(subjects_final_grades):
    for subject, grade in subjects_final_grades.items():
        if grade == FAILED_GRADE:
            return promotion_status.FAILED

    return promotion_status.PASSED

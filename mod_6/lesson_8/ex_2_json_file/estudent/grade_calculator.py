from estudent.errors import LogicError


class GradeCalculator:

    MAX_FAILING_GRADES_TO_PASS = 2

    @staticmethod
    def normal_promotion_policy(final_grades):
        failing_grades = GradeCalculator.get_number_of_failing_grades(final_grades)
        if failing_grades > GradeCalculator.MAX_FAILING_GRADES_TO_PASS:
            return False
        return True

    @staticmethod
    def strict_promotion_policy(final_grades):
        failing_grades = GradeCalculator.get_number_of_failing_grades(final_grades)
        if failing_grades > GradeCalculator.MAX_FAILING_GRADES_TO_PASS:
            return False
        if GradeCalculator.calculate_student_avg(final_grades) < 3:
            return False
        return True

    @staticmethod
    def get_number_of_failing_grades(grades):
        failing_grades = 0
        for grade in grades:
            if not grade.is_passing():
                failing_grades += 1
        return failing_grades

    @staticmethod
    def calculate_student_avg(final_grades):
        if len(final_grades) < 1:
            raise LogicError("Nie można obliczyć średniej jeżeli uczeń nie posiada żadnych ocen")
        grade_sum = 0
        for grade in final_grades:
            grade_sum += grade.value
        return grade_sum / len(final_grades)

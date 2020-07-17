
def find_best_grade(subjects_with_final_grades):
    best_subject = None
    best_final_grade = 0
    # for subject, final_grade in subjects_with_final_grades.items():
    #     if final_grade > best_final_grade:
    #         best_final_grade = final_grade
    #         best_subject = subject
    # return best_subject, best_final_grade

    # for element in subjects_with_final_grades.items():
    #     print(type(element))
    #     subject = element[0]
    #     final_grade = element[1]
    #     if final_grade > best_final_grade:
    #         best_final_grade = final_grade
    #         best_subject = subject
    # return best_subject, best_final_grade

def run_avg_speed(name, distance, time):
    avg_speed = distance / time
    print(f"{name} biega z prędkością {avg_speed}")

#
# def sum_numbers(*args):
#     print(type(args))
#     return sum(args)


def run_example():
    # sum_numbers(1, 2, 3, 4, 5, 6)

    # subjects_with_final_grades = {
    #     "Matematyka": 4,
    #     "Historia": 5,
    #     "Fizyka": 3,
    #     "Biologia": 4
    # }
    #
    # best_subject, best_grade = find_best_grade(subjects_with_final_grades)
    # print(best_subject, best_grade)
    # result = find_best_grade(subjects_with_final_grades)
    # print(result)
    # print(type(result))

    run_data = ("Bob", 20, 2)
    run_avg_speed(*run_data)


if __name__ == '__main__':
    run_example()
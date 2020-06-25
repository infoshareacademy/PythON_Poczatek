
from estudent_book.grades.actions import check_student_promotion

# print("Witaj w elektronicznym dzienniku!")
#
# option = None
# while option != "X":
#     check_student_promotion()
#     option = input("Aby przerwać wprowadź 'X': ")


def run_estudent_book():
    print("Witaj w elektronicznym dzienniku!")

    option = None
    while option != "X":
        check_student_promotion()
        option = input("Aby przerwać wprowadź 'X': ")


if __name__ == '__main__':
    run_estudent_book()

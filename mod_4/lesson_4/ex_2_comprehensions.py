import random


def run_example():
    # Analogicznie do list comprehensions działa dict comprehensions
    expenditures_names = ["prąd", "woda", "zakupy"]
    expenditures = {expenditure_name: random.randint(1, 100) for expenditure_name in expenditures_names}
    print(expenditures)

    # Tu również możemy skorzystać z instrukcji warunkowej
    # student_names = ["Alicja", "Robert", "Mikołaj", "Konstanty"]
    # students = {random.randint(1, 100): name for name in student_names}
    # print(students)

    # students = {
    #     random.randint(1, 100): name if len(name) < 8 else f"{name[:5]}..."
    #     for name in student_names
    # }
    # print(students)

    # new_students = {identifier * 10: f"{name[:1]}..." for identifier, name in students.items()}
    # print(new_students)


if __name__ == '__main__':
    run_example()

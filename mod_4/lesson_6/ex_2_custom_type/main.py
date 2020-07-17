from estudent import data_generator


def run_example():
    students = data_generator.generate_students(number_of_students=20)

    students[0].first_name = "Bob"
    students[0].last_name = "Kowalski"

    bob = students[0]
    also_bob = students[0]

    print("students[0]:", students[0])
    print("bob:", bob)
    print("also_bob:", also_bob)

    print(id(students[0]))
    print(id(bob))
    print(id(also_bob))

    print()
    print("Bob zmienia imię...")
    bob.first_name = "Robert"

    print("students[0]:", students[0])
    print("bob:", bob)
    print("also_bob:", also_bob)

    print(id(students[0]))
    print(id(bob))
    print(id(also_bob))


if __name__ == '__main__':
    run_example()


class Teacher:

    def __init__(self, name, subject):
        print("Wywołano konstruktor klasy bazowej!")
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"


class Tutor(Teacher):
    # pass

    # def __init__(self, name, subject):
    #     print("To ja - konstruktor klasy potomnej")
    #     super().__init__(name, subject)
    #     print(f"Tutaj jest dostęp do pól klasy bazowej: name={self.name}")

    # def __init__(self, name, subject):
    #     print(f"A tu jeszcze nie ma dostępu do pól klasy bazowej {self.name}")
    #     super().__init__(name, subject)

    def __init__(self, name, subject):
        pass


def run_example():
    tutor = Tutor(name="Jakub", subject="Historia")

    print(f"Wychowawca nazywa się {tutor.name}")
    tutor.assign_department("B1")


if __name__ == '__main__':
    run_example()
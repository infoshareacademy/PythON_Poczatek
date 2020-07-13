
class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"


class Tutor(Teacher):

    def __init__(self, name, subject, department):
        # Nadpisania wartości pola należy dokonać po wywołaniu konstruktora klasy bazowej
        # Inaczej konstrutor klasy bazowej nadpisze naszą wartość
        # self.assigned_departments = [department]
        super().__init__(name, subject)
        self.guided_department = department
        # self.assigned_departments = [department]
        # W przypadku, gdy dane pole jest listą, możemy je zmodyfikować/rozszerzyć np. dodając wartość
        self.assigned_departments.append(department)

    def send_message_from_parents(self, message):
        print(f"Wiadomość od rodziców wysłana: '{message}'")

    def __str__(self):
        return f"Wychowawca klasy {self.guided_department} i nauczyciel przedmiotu {self.subject} - {self.name}. " \
               f"Uczy klasy: {self.assigned_departments}"


def run_example():
    tutor = Tutor(department="A2", name="Jakub", subject="Historia")
    tutor.assign_department("B1")
    print(tutor)


if __name__ == '__main__':
    run_example()

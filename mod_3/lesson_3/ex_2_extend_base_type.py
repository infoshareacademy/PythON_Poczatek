
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

    # def __init__(self, name, subject, department):
    #     # Odwołanie do konstruktora klasy bazowej
    #     super().__init__(name, subject)
    #     # Rozszerzenie klasy bazowej o dodatkowe pola
    #     self.guided_department = department

    def __init__(self, department, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guided_department = department

    # Rozszerzenie klasy bazowej o dodatkowe metody
    def send_message_from_parents(self, message):
        print(f"Wiadomość od rodziców wysłana: '{message}'")


def run_example():
    tutor = Tutor(department="A2", name="Jakub", subject="Historia")
    tutor.assign_department("A2")
    tutor.assign_department("B1")
    print(f"Wychowawca: {tutor}")

    print(tutor.guided_department)
    tutor.send_message_from_parents(message="Pozdrowienia!")


if __name__ == '__main__':
    run_example()

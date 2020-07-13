
class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []
        self.__private_info = "Dane prywatne klasy bazowej"

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"


class Tutor(Teacher):

    def __init__(self, name, subject, department):
        super().__init__(name, subject)
        self.guided_department = department

    def send_message_from_parents(self, message):
        print(f"Wiadomość od rodziców wysłana: '{message}'")

    def access_to_private_info(self):
        print(self.__private_info)


def run_example():
    # Obiekt klasy potomnej ma dostęp do metod i pól swojej klasy oraz klasy bazowej
    tutor = Tutor(department="A2", name="Jakub", subject="Historia")
    # print(tutor.guided_department)
    # tutor.send_message_from_parents(message="Pozdrowienia!")
    # tutor.assign_department("A2")
    # tutor.assign_department("B1")
    # print(tutor.name)
    # print(tutor.assigned_departments)

    # Obiekt klasy bazowej ma dostęp tylko do pól i metod swojej klasy
    # teacher = Teacher(name="Jakub", subject="Historia")
    # # print(teacher.guided_department)
    # # teacher.send_message_from_parents(message="Pozdrowienia!")
    # teacher.assign_department("C1")
    # print(teacher.name)
    # print(teacher.assigned_departments)

    # Obiekt klasy potomnej nie ma dostępu do metod i pól prywatnych klasy bazowej
    # print(tutor.__private_info)
    tutor.access_to_private_info()


if __name__ == '__main__':
    run_example()

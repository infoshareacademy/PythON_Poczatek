
class Teacher:

    def __init__(self, name, subject, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"


class OfficeWorker:

    def __init__(self, mailbox):
        self.mailbox = mailbox

    def send_email(self, message):
        print(f"Wysłano wiadomość na skrzynkę {self.mailbox} o treści: {message}")


class Director(Teacher, OfficeWorker):
    pass


def run_example():
    director = Director(name="Jakub", subject="Matematyka", mailbox="adres-email")
    print(director)
    director.send_email("Gratulacje")


if __name__ == '__main__':
    run_example()

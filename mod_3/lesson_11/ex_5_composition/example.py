
class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.assigned_departments = []

    def assign_department(self, department):
        self.assigned_departments.append(department)

    def __str__(self):
        return f"Nauczyciel przedmiotu {self.subject} - {self.name}. Uczy klasy: {self.assigned_departments}"


class OfficeAccess:

    def __init__(self, mailbox, username, password):
        self.mailbox = mailbox
        self.password = password
        self.username = username
        self.authorized = False

    def authorize(self, username, password):
        self.authorized = username == self.username and password == self.password

    def send_email(self, message, dst_mailbox):
        if self.authorized:
            print(f"Wysłano wiadomość ze skrzynki {self.mailbox} do {dst_mailbox} o treści: {message}")
        else:
            print("Wymagane uwierzytelnienie")


class Director(Teacher):

    def __init__(self, name, subject, mailbox, username, password):
        super().__init__(name, subject)
        self.office_access = OfficeAccess(mailbox, username, password)

    def contact_with_parents(self, message, parents_emails):
        for mailbox in parents_emails:
            self.office_access.send_email(message, mailbox)

    def login(self, provided_username, provided_password):
        self.office_access.authorize(provided_username, provided_password)


def run_example():
    director = Director(name="Jakub", subject="Matematyka", mailbox="adres-email", username="jakub", password="pass")
    parents_emails = [
        "rodzic-1-email",
        "rodzic-2-email",
        "rodzic-3-email",
    ]
    director.login(provided_username="jakub", provided_password="pass")
    director.contact_with_parents(message="Zapraszam na wywiadówkę", parents_emails=parents_emails)


if __name__ == '__main__':
    run_example()

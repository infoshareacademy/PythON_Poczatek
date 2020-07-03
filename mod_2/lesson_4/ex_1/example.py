
class Student:

    def __init__(self, name):
        self.name = name

    def print_something(self):
        print("To ja - metoda studenta!")

    def print_self(self):
        print("Czym jest self?: ", self)
        print("Jest tutaj dostęp do name:", self.name)
    #
    def do_all_work(self):
        print("Teraz to się napracuję...")
        self.do_piece_of_work()
        self.do_piece_of_work()
        self.do_piece_of_work()
        print("Koniec :)")

    def do_piece_of_work(self):
        print("Robota...")


def run_example():
    student = Student(name="Mikołaj")
    # Wywołanie metody
    student.print_something()

    # Pierwszy przekazany niejawnie argument, zawiera referencję na aktualny obiekt
    student.print_self()

    # Metoda może wołać inną metodę
    student.do_all_work()


if __name__ == '__main__':
    run_example()

class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def promote(self):
        self.promoted = True

    def print_self(self):
        print(f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}")


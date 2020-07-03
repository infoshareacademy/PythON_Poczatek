class Grade:

    def __init__(self, value):
        self.value = value

    def is_passing(self):
        return self.value > 1

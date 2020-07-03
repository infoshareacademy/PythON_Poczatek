class Grade:

    FAILING_GRADE = 1

    def __init__(self, value):
        self.value = value

    def is_passing(self):
        return self.value > Grade.FAILING_GRADE

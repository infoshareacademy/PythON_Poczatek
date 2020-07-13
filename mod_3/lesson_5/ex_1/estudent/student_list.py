
class StudentList(list):

    @property
    def first_student(self):
        if len(self):
            return self[0]
        return None

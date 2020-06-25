
students = [
    {
        "name": "Jakub",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "fizyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "historia",
                "grades": [2, 3, 5, 1, 3, 5]
            }
        ]
    },
    {
        "name": "Mikołaj",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "fizyka",
                "grades": [2, 3, 5, 1, 3, 5]
            },
            {
                "subject": "historia",
                "grades": [2, 1, 1, 1, 2, 1]
            }
        ]
    }
]


def find_student_by_name(name):
    for student in students:
        if student["name"] == name:
            return student


def is_student_in_school(name):
    if not find_student_by_name(name):
        return False
    return True

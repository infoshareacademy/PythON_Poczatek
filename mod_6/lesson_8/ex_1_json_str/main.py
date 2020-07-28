import dataclasses
import json

from estudent import data_generator


def run_example():
    students = data_generator.generate_students(number_of_students=10)
    students_data = {
        "students": [
            {
                "first_name": student.first_name,
                "last_name": student.last_name,
                "promoted": student.promoted,
                "final_grades": [dataclasses.asdict(grade) for grade in student.final_grades],
            }
            for student in students
        ]
    }
    json_students = json.dumps(students_data)
    print(json_students)
    print(type(json_students))
    # print(json.dumps(students_data, indent=4))

    print(json.loads(json_students))
    print(type(json.loads(json_students)))


if __name__ == "__main__":
    run_example()

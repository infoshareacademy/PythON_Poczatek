from typing import List

from pydantic.dataclasses import dataclass


@dataclass
class Student:
    identifier: int
    first_name: str
    last_name: str


@dataclass
class School:
    name: str
    students: List[Student]


def run_example():
    school_data = {
        "name": "Wesoła Szkoła",
        "students": [
            {
                "identifier": None,
                "first_name": "Bob",
                "last_name": "Kowalski",
            },
            {
                "identifier": 220,
                "first_name": "Alicja",
                "last_name": "Nowak",
            }
        ]
    }
    school = School(**school_data)
    print(school)


if __name__ == '__main__':
    run_example()

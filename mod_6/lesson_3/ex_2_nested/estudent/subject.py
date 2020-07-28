from dataclasses import dataclass, field
from typing import List


@dataclass
class Subject:
    identifier: int
    name: str
    is_obligatory: bool = True
    teachers_names: List[str] = field(default_factory=list)

    def assign_teacher(self, name):
        self.teachers_names.append(name)

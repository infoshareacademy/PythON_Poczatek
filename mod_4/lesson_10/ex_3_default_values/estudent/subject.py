from dataclasses import dataclass


@dataclass
class Subject:
    identifier: int
    name: str
    is_obligatory: bool = True

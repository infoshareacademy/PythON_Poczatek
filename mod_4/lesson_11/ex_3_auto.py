from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Color(AutoName):
    BLUE = auto()
    GREEN = auto()
    RED = auto()

#
# class Color(Enum):
#     BLUE = auto()
#     GREEN = auto()
#     RED = auto()


def run_example():
    blue = Color.BLUE
    green = Color.GREEN
    print(blue.name, blue.value)
    print(green.name, green.value)


if __name__ == '__main__':
    run_example()

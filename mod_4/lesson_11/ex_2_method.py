from enum import Enum


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def is_weekend(self):
        return self.value > 5

    def is_earlier_in_week(self, other_day):
        return self.value < other_day.value


def run_example():
    monday = Week.MONDAY
    saturday = Week.SATURDAY
    print(monday.is_weekend())
    print(saturday.is_weekend())


if __name__ == '__main__':
    run_example()

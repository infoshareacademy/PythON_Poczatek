from enum import Enum


class WeekStr:
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


def is_weekend_str(week_day):
    return week_day == WeekStr.SATURDAY or week_day == WeekStr.SUNDAY


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    

def is_weekend(week_day):
    return week_day is Week.SATURDAY or week_day is Week.SUNDAY


def run_example():
    # friday = Week.FRIDAY
    # print(friday)
    # print(friday.name, friday.value)
    #
    # print(friday is Week.FRIDAY)
    # print(friday is Week.MONDAY)

    # print(is_weekend(Week.SUNDAY))
    # print(is_weekend_str(WeekStr.SUNDAY))
    #
    # print(is_weekend_str("SUNDAY"))
    # print(is_weekend(7))
    # print(is_weekend("SUNDAY"))
    #
    # print(is_weekend_str("Sunday"))

    day_of_week_number = int(input("Który jest dzień tygodnia? "))
    day_of_week = Week(day_of_week_number)
    print(day_of_week)

    day_of_week_from_name = Week["FRIDAY"]
    print(day_of_week_from_name)
    print(type(day_of_week_from_name))


if __name__ == '__main__':
    run_example()

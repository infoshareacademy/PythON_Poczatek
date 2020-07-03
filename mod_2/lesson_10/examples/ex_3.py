

def calculate_sum_via_args(*args):
    result = 0
    for number in args:
        result += number
    return result


def add_two_numbers(first, second):
    return first + second


def run_example():
    numbers = [1, 2, 3, 4, 5, 6]

    result = calculate_sum_via_args(numbers)
    print(result)

    # result = calculate_sum_via_args(*numbers)
    # print(result)

    # two_numbers = [10, 30]
    # result = add_two_numbers(*two_numbers)
    # print(result)

    # combined_numbers = [*numbers, *two_numbers]
    # print(combined_numbers)



if __name__ == '__main__':
    run_example()
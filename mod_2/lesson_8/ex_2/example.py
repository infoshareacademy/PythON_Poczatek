import random


def say_hello():
    print("Hello World!")


def say_good_bye():
    print("Good bye!")


def randomize_func(first_func, second_func):
    number = random.randint(1, 2)
    if number == 1:
        return first_func
    return second_func


def run_example():
    hello_or_good_bye = randomize_func(say_hello, say_good_bye)
    hello_or_good_bye()


if __name__ == '__main__':
    run_example()

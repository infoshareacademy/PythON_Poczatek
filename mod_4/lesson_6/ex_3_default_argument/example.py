
def func_with_default_immutable(number=2):
    number += 1
    print(number)


def func_with_default_mutable(numbers=[]):
    numbers.append(1)
    print(numbers)


def run_example():

    func_with_default_immutable()
    func_with_default_immutable()
    func_with_default_immutable()

    func_with_default_mutable()
    func_with_default_mutable()
    func_with_default_mutable()


if __name__ == '__main__':
    run_example()

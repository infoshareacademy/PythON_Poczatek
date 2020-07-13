
class Grandparent:

    def say_hello(self):
        print("Grandpa says Hello!")


class ParentOne(Grandparent):
    # pass

    def say_hello(self):
        print("ParentOne says Hello!")


class ParentTwo(Grandparent):
    # pass

    def say_hello(self):
        print("ParentTwo says Hello!")


class Child(ParentOne, ParentTwo):
    pass

    # def say_hello(self):
    #     print("To young to talk")


def run_example():
    child = Child()
    child.say_hello()


if __name__ == '__main__':
    run_example()

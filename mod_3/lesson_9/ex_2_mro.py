class Grandparent:

    def say_hello(self):
        print("Grandpa says Hello!")


class ParentOne(Grandparent):

    def say_hello(self):
        print("ParentOne says Hello!")


class ParentTwo(Grandparent):

    def say_hello(self):
        print("ParentTwo says Hello!")


class Child(ParentOne, ParentTwo):
    pass


def run_example():
    print(Child.mro())


if __name__ == '__main__':
    run_example()

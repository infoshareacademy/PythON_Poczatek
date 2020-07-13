class Grandparent:

    def say_hello(self):
        print("Grandpa says Hello!")


class ParentOne(Grandparent):

    def say_hello(self):
        print("ParentOne says Hello!")


class Child(Grandparent, ParentOne):
    pass


def run_example():
    child = Child()
    child.say_hello()


if __name__ == '__main__':
    run_example()

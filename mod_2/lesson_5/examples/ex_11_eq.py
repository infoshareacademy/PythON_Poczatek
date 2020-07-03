
class Money:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def as_cents(self):
        return self.dollars * 100 + self.cents

    def __str__(self):
        return f"{self.dollars}$ and {self.cents} cents"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() == other.as_cents()


def compare_money_lists(first, second):
    for money in first:
        if money not in second:
            return False
    return True


def run_example():
    some_money = [
        Money(dollars=1, cents=20),
        Money(dollars=10, cents=20),
        Money(dollars=100, cents=20),
        Money(dollars=1000, cents=20),
    ]
    # print(f"{Money(dollars=1, cents=20)} in some_money?")
    # print(Money(dollars=1, cents=20) in some_money)
    #
    # print(f"{Money(dollars=55, cents=20)} in some_money?")
    # print(Money(dollars=55, cents=20) in some_money)

    other_money = [
        Money(dollars=1000, cents=20),
        Money(dollars=100, cents=20),
        Money(dollars=10, cents=20),
        Money(dollars=10, cents=20),
    ]

    print(compare_money_lists(some_money, other_money))


if __name__ == '__main__':
    run_example()

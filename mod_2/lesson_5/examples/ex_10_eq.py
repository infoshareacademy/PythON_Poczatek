
class Money:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def as_cents(self):
        return self.dollars * 100 + self.cents

    def __str__(self):
        return f"{self.dollars}$ and {self.cents} cents"

    # def __eq__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return self.as_cents() == other.as_cents()
    #
    # def __ne__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return self.as_cents() != other.as_cents()
    #
    # def __lt__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return self.as_cents() < other.as_cents()
    #
    # def __le__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return self.as_cents() <= other.as_cents()
    #
    # def __gt__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return self.as_cents() > other.as_cents()
    #
    # def __ge__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return self.as_cents() >= other.as_cents()


def run_example():
    print(f"{Money(dollars=1, cents=20)} == {Money(dollars=100, cents=5)}?")
    print(Money(dollars=1, cents=20) == Money(dollars=100, cents=5))

    print(f"{Money(dollars=100, cents=5)} == {Money(dollars=100, cents=5)}?")
    print(Money(dollars=100, cents=5) == Money(dollars=100, cents=5))

    # print(f"{Money(dollars=100, cents=5)} != {Money(dollars=100, cents=5)}?")
    # print(Money(dollars=100, cents=5) != Money(dollars=100, cents=5))
    #
    # print(f"{Money(dollars=1, cents=20)} < {Money(dollars=100, cents=5)}?")
    # print(Money(dollars=1, cents=20) < Money(dollars=100, cents=5))
    #
    # print(f"{Money(dollars=1, cents=20)} <= {Money(dollars=100, cents=5)}?")
    # print(Money(dollars=1, cents=20) <= Money(dollars=100, cents=5))
    #
    # print(f"{Money(dollars=1, cents=20)} > {Money(dollars=100, cents=5)}?")
    # print(Money(dollars=1, cents=20) > Money(dollars=100, cents=5))
    #
    # print(f"{Money(dollars=1, cents=20)} >= {Money(dollars=100, cents=5)}?")
    # print(Money(dollars=1, cents=20) >= Money(dollars=100, cents=5))
    #
    # some_money = [
    #     Money(dollars=1, cents=20),
    #     Money(dollars=10, cents=20),
    #     Money(dollars=100, cents=20),
    #     Money(dollars=1000, cents=20),
    #     Money(dollars=10000, cents=20),
    # ]
    # print(f"{Money(dollars=1, cents=20)} in some_money?")
    # print(Money(dollars=1, cents=20) in some_money)
    #
    # print(f"{Money(dollars=55, cents=20)} in some_money?")
    # print(Money(dollars=55, cents=20) in some_money)




if __name__ == '__main__':
    run_example()

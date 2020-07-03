
class Money:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def as_cents(self):
        return self.dollars * 100 + self.cents

    def __add__(self, other):
        all_cents = self.as_cents() + other.as_cents()
        dollars = int(all_cents / 100)
        cents = all_cents % 100
        return Money(dollars, cents)

    def __str__(self):
        return f"{self.dollars}$ and {self.cents} cents"


def run_example():
    some_money = Money(dollars=100, cents=55)
    extra_money = Money(dollars=5, cents=80)
    all_money = some_money + extra_money
    print(all_money)


if __name__ == '__main__':
    run_example()

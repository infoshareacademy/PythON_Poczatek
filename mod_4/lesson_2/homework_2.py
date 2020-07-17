
#  Napisz funkcję generującą losowy identyfikator.
#  Identyfikator powinien być w formacie 00001, tzn. zawsze o długości  pięciu znaków,
#  dopełniony z lewej strony odpowiednią liczbą zer.
import random


def run_example():
    identifier_number = random.randint(1, 9999)
    identifier = str(identifier_number).zfill(5)

    print(f"Twój identyfikator to: {identifier}")


if __name__ == '__main__':
    run_example()

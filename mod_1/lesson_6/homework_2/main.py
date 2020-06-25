
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta
# na podstawie otrzymanych długości przyprostokątnych.
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
# Wykorzystaj w tym celu moduł math z biblioteki standardowej i oraz funkcje sqrt i pow
import math


def calculate_c_len(a_len, b_len):
    return math.sqrt(math.pow(a_len, 2) + math.pow(b_len, 2))


a = float(input("Jaka jest długość boku a? "))
b = float(input("Jaka jest długość boku b? "))

c = calculate_c_len(a, b)
print(f"Długość przeciwprostokątnej to {c}")



# Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby całkowite z przedziału od 1 do 10.
# Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).
# Kolejne trzy liczby typu float podnieś do potęgi o wartości
# odpowiednio pierwszej, drugiej i trzeciej wylosowanej liczby całkowitej.
import math
import random


def run_example():
    float_numbers = []
    for _ in range(6):
        float_numbers.append(random.uniform(-20, 20))
    print(float_numbers)

    int_numbers = []
    for _ in range(3):
        int_numbers.append(random.randint(1, 10))
    print(int_numbers)

    print(round(float_numbers[0]))
    print(math.ceil(float_numbers[1]))
    print(math.floor(float_numbers[2]))

    print(float_numbers[3] ** int_numbers[0])
    print(pow(float_numbers[4], int_numbers[1]))
    print(math.pow(float_numbers[5], int_numbers[2]))

    # print(int_numbers[0] ** int_numbers[0])
    # print(math.pow(int_numbers[0], int_numbers[0]))


if __name__ == '__main__':
    run_example()
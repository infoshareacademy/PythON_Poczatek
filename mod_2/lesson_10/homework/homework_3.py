
# Wygeneruj dwie listy zawierające losowe liczby całkowite i połącz je w jedną wykorzystując operator *
import random


def generate_random_numbers():
    result = []
    for _ in range(random.randint(5, 10)):
        result.append(random.randint(1, 100))
    return result


def run_homework():
    random_numbers = generate_random_numbers()
    other_numbers = generate_random_numbers()
    print(random_numbers)
    print(other_numbers)

    all_numbers = [*random_numbers, *other_numbers]
    print(all_numbers)


if __name__ == '__main__':
    run_homework()
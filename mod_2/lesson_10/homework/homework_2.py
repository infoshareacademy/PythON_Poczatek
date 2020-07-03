
# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych
# i wypisze sposób w jaki została wywołana,
# tzn. poszczególne nazwy argumentów, znak równa się i wartość (np. first_name=Mikołaj, age=134)


def print_call_str(**kwargs):
    call_str = "print_call_str("
    for argument_name, argument_value in kwargs.items():
        call_str += f"{argument_name}={argument_value}, "
    call_str += ")"
    print(call_str)


def run_homework():
    print_call_str(argument="i jego wartość", a_to_inny="wartość też inna")


if __name__ == '__main__':
    run_homework()

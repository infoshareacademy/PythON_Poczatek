
# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.
# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.


def print_call_str(**kwargs):
    call_str = "print_call_str("
    for argument_name, argument_value in kwargs.items():
        call_str += f"{argument_name}={argument_value}, "
    call_str += ")"
    print(call_str)


def run_homework():
    english_polish = {
        "storm": "burza",
        "chair": "krzesło",
        "head": "głowa"
    }

    english_polish_colors = {
        "green": "zielony",
        "blue": "niebieski",
        "red": "czerwony",
    }

    english_polish_words = {**english_polish, **english_polish_colors}
    print(english_polish_words)

    print_call_str(**english_polish_words)


if __name__ == '__main__':
    run_homework()

# Wykorzystaj bibliotekę requests do pobrania strony infoshareacademy.com
# Wypisz treść (kod HTML) pobranej strony

import requests


def run_homework():
    try:
        response = requests.get("https://infoshareacademy.com/")
    except requests.RequestException as error:
        print(f"Błąd przy połączeniu: {error}")
        return

    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        print(f"Żądanie zakończone niepowodzeniem {error}")
        return

    print(response.text)


if __name__ == '__main__':
    run_homework()

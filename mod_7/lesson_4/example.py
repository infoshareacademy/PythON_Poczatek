import requests


# def run_example():
#     # response = requests.get("https://www.pyjazz.pl")
#     response = requests.get("https://github.com/fsfefe")
#     print(response.status_code)
#     print(response.ok)
#
#     response.raise_for_status()
#     print(response.text)


def run_example():
    try:
        # response = requests.get("https://www.pyjazz.pl")
        response = requests.get("https://github.com/fsfefe")
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
    run_example()

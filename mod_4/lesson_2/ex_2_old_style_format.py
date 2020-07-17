

def run_example():
    # fstringi zostały wprowadzone w Pythonie 3.6
    language = "Python"
    python_age = 30
    message = f"{language} ma już prawie {python_age} lat"
    print(message)

    # Wcześniejszym sposobem na formatowanie napisów jest tzw. New style formatting, czyli metoda format na str
    # Występuje ona w kilku wariantach - po pierwsze puste nawiasy i uzupełnianie według kolejności
    # message = "{} ma już prawie {} lat".format(language, python_age)
    # print(message)

    # Kolejność nie może nam się pomylić
    # message = "{} ma już prawie {} lat".format(python_age, language)
    # print(message)

    # Drugi sposób to podanie wprost kolejności argumentów
    # message = "{0} ma już prawie {1} lat".format(language, python_age)
    # print(message)

    # Trzeci sposób to nazwanie poszczególnych zmiennych - wtedy nie musimy się martwić kolejnością
    # message = "{language} ma już prawie {age} lat".format(language=language, age=python_age)
    # print(message)

    # Innym sposobem formatowania jest tzw. printf style, czyli formatowanie z procentem
    # W tym przypadku za pomocą literek możemy podać typ zmiennej (s -> str, d -> int)
    # message = "%(language)s ma już prawie %(age)d lat" % {"language": language, "age": python_age}
    # print(message)

    # Tutaj również istnieje wariant bez nazw - argumenty przekazujemy za pomocą krotki
    # message = "%s ma już prawie %d lat" % (language, python_age)
    # print(message)



if __name__ == '__main__':
    run_example()

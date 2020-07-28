#
# Rozbuduj rozwiązanie zadania trzeciego z lekcji trzeciej (łapanie wyjątków) o utrwalanie złożonych zamówień.
# Przed wyłączeniem programu dopisz złożone zamówienie (wynik wykonania str na obiekcie zamówienia) do pliku orders.txt.
# Plik orders.txt powinien znajdować się w katalogu data - wykorzystaj ścieżkę względną by się do niego odwołać

from shop import user_interface


def run_homework():
    user_interface.handle_customer()


if __name__ == '__main__':
    run_homework()

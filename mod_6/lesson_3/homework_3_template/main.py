#
# Uzupełnij szablon kodu o odpowiednie implementacje (oznaczenia TODO)
#  - Funkcje z user_interface po uruchomieniu programu zapytają użytkownika o dane (imię i nazwisko)
#  a następnie zaproponują dodanie kolejnych towarów do zamówienia.
#  - W celu kontroli dostępności towarów klasa Store, posiada zdefiniowaną listę dostępnych produktów i ich liczbę.
#  Podczas dodawania kolejnych produktów do zamówienia aktualizuj ich stan w Store i gdyby okazało się,
#  że nie można zrealizować oczekiwań klienta wyrzuć odpowiedni wyjątek i obsłuż go komunikatem dla użytkownika.
from shop import user_interface


def run_homework():
    user_interface.handle_customer()


if __name__ == '__main__':
    run_homework()

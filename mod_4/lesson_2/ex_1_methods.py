
def run_example():
    # Metoda join stosuje podany string jako łącznik do scalenia listy napisów w jeden
    account_number_parts = ["1234", "4567", "8910", "8910", "4567", "1234"]
    print("-".join(account_number_parts))
    # Pusty napis też może być łącznikiem
    print("".join(account_number_parts))

    # Metody lstrip, rstrip oraz strip usuwają znaki odpowiednio z lewej, prawej i obu stron napisu
    # name = "   Mikołaj   "
    # left_clear = name.lstrip()
    # right_clear = name.rstrip()
    # both_clear = name.strip()
    # print(f"{left_clear} Lewandowski")
    # print(f"{right_clear} Lewandowski")
    # print(f"{both_clear} Lewandowski")

    # Każda z tych metod przyjmuje też ciąg znaków - jeżeli znajdzie którykolwiek z nich usuwa itd.
    # Domyślnie usuwa odstępy
    # name = " -|  Mikołaj |-  "
    # left_clear = name.lstrip("-| ")
    # right_clear = name.rstrip("-| ")
    # both_clear = name.strip("-| ")
    # print(f"{left_clear} Lewandowski")
    # print(f"{right_clear} Lewandowski")
    # print(f"{both_clear} Lewandowski")

    # Metody startswith oraz endswith sprawdzają czy dany napis odpowiednio zaczyna i kończy się prefixem/suffixem
    # Opcjonalne argumenty pozwalają podać inny niż początek/koniec napisu zakres wyszukiwania
    # last_name = "Lewandowski"
    # print(last_name.startswith("Lew"))
    # print(last_name.startswith("Kow"))
    # print(last_name.endswith("ski"))
    # print(last_name.endswith("ak"))

    # Metoda zfill "dopełnia" napis zerami do osiągnięcia podanej długości.
    # Jest to przydatne np. do budowania identyfikatorów o określonym formacie
    # number = 135
    # identifier = str(number).zfill(8)
    # print(identifier)

    # Metody find oraz index pozwalają pierwszy indeks pod którym występuje ciąg znaków w napisie
    # sentence = "Ale dzisiaj ładny dzień! Wczoraj też był dobry dzień."
    # print(sentence.find("dzień"))
    # print(sentence.index("dzień"))

    # Opcjonalne argumenty pozwalają podać inny zakres wyszukiwania
    # (wyszukiwanie w części napisu [start:end] - domyślnie od początku do końca)
    # print(sentence.find("dzień", 20))
    # print(sentence.index("dzień", 24))

    # Index działa tak samo jak find, przy czym jeżeli ciąg znaków nie zostanie znaleziony
    # find zwraca -1 a index rzuca błąd
    # print(sentence.find("Tego tam nie ma"))
    # print(sentence.index("Tego tam nie ma"))


if __name__ == '__main__':
    run_example()

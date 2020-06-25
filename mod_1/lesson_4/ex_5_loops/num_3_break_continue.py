
# Poszukiwanie elementu w zbiorze
# expenditures = [120, 300, 250.45, 3000, 50, 75]
#
# for expenditure in expenditures:
#     print(expenditure)
#     if expenditure > 1000:
#         print("Drogi wydatek znaleziony!")
#         break

# Wypisywanie co drugiego sportu
favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
for index, sport in enumerate(favourite_sports):
    if index % 2 != 0:
        continue
    print(sport)

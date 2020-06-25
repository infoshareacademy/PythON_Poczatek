
# Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i pokonanego dystansu
# i umieść ją w jednym pliku. W drugim pliku zaimportuj funkcję,
# wczytaj informacje od użytkownika i oblicz prędkość średnią

import speed_calculator

running_distance = float(input("Ile km przebiegłeś/przebiegłaś? "))
running_time = float(input("Ile godzin Ci to zajęło? "))

avg_speed = speed_calculator.avg_speed(running_distance, running_time)
print(f"Twoja średnia prędkość biegu to {avg_speed}km/h")

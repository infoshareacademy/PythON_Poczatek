
income = 5000
employees_number = 7
years_on_the_market = 3

if income < 5000:
    print("Przyznano główne wsparcie")
elif 5 <= employees_number <= 10:
    print("Przyznano wsparcie z funduszu pracowników")
elif years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm")
elif income == 6578:
    print("Przyznano wsparcie niespodziankę")
else:
    print("Przyznano wsparcie na pocieszenie ;)")

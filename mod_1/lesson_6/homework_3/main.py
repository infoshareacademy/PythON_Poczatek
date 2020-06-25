import calculations.investment


def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)


print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value = ask_for_int_value("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
percentage = ask_for_int_value("Jakie jest oprocentowanie (%)? ")
years = ask_for_int_value("Ile lat trwa lokata? ")

final_value = calculations.investment.calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

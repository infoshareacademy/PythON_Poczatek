
# Import modułów w pakiecie czy też sub pakietów wykonujemy za pomocą kropki
import home_budget.calculations.expenditures
import home_budget.data_parsers.csv_format

all_expenditures = home_budget.data_parsers.csv_format.load_expenditures()
expenditures_week_by_week = home_budget.calculations.expenditures.calculate_week_by_week(all_expenditures)
print(expenditures_week_by_week)


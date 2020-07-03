class TaxRates:

    FRUITS_AND_VEGETABLES = 0.05
    FOOD = 0.08
    ALL = 0.2


class TaxCalculator:

    @staticmethod
    def tax_for_order_element(order_element):
        product_category = order_element.product.category_name
        if product_category == "Owoce i Warzywa":
            tax_rate = TaxRates.FRUITS_AND_VEGETABLES
        elif product_category == "Jedzenie":
            tax_rate = TaxRates.FOOD
        else:
            tax_rate = TaxRates.ALL
        return tax_rate * order_element.calculate_price()


#
# class TaxCalculator:
#
#     TAX_RATES = {
#         "Owoce i Warzywa": 0.05,
#         "Jedzenie": 0.08,
#     }
#     BASE_TAX_RATE = 0.2
#
#     @staticmethod
#     def tax_for_order_element(order_element):
#         product_category = order_element.product.category_name
#         if product_category in TaxCalculator.TAX_RATES:
#             tax_rate = TaxCalculator.TAX_RATES[product_category]
#         else:
#             tax_rate = TaxCalculator.BASE_TAX_RATE
#         return tax_rate * order_element.calculate_price()

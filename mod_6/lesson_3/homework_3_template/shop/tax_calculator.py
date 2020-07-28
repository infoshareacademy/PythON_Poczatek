
class TaxCalculator:

    TAX_RATES = {
        "Owoce i Warzywa": 0.05,
        "Jedzenie": 0.08,
    }
    BASE_TAX_RATE = 0.2

    @staticmethod
    def tax_for_order_element(order_element):
        product_category = order_element.product.category_name
        if product_category in TaxCalculator.TAX_RATES:
            tax_rate = TaxCalculator.TAX_RATES[product_category]
        else:
            tax_rate = TaxCalculator.BASE_TAX_RATE
        return tax_rate * order_element.calculate_price()

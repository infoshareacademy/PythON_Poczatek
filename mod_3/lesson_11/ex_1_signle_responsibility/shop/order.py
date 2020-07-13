
from shop.order_element import OrderElement


class Order:
    MAX_ELEMENTS = 5

    TAX_RATES = {
        "Owoce i Warzywa": 0.05,
        "Jedzenie": 0.08,
    }
    BASE_TAX_RATE = 0.2

    NO_DISCOUNT_POLICY = "NO_DISCOUNT"
    PERCENTAGE_DISCOUNT = "PERCENTAGE_DISCOUNT"
    ABSOLUTE_DISCOUNT = "ABSOLUTE_DISCOUNT"

    def __init__(
            self,
            client_first_name,
            client_last_name,
            order_elements=None,
            discount_policy="NO_DISCOUNT",
            discount_percentage=0,
            discount_value=0,
    ):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if order_elements is None:
            order_elements = []
        self._order_elements = order_elements

        self.discount_policy = discount_policy
        self.discount_value = discount_value
        self.discount_percentage = discount_percentage

    def apply_no_discount(self, total_price):
        return total_price

    def apply_percentage_discount(self, total_price):
        return total_price * (100 - self.discount_percentage) / 100

    def apply_absolute_discount(self, total_price):
        if total_price < self.discount_value:
            return 0
        return total_price - self.discount_value

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()

        if self.discount_policy == Order.PERCENTAGE_DISCOUNT:
            return self.apply_percentage_discount(total_price)
        elif self.discount_policy == Order.ABSOLUTE_DISCOUNT:
            return self.apply_absolute_discount(total_price)
        else:
            return self.apply_no_discount(total_price)

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_ELEMENTS:
            self._order_elements = value
        else:
            self._order_elements = value[:Order.MAX_ELEMENTS]

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ELEMENTS:
            new_element = OrderElement(product, quantity)
            self._order_elements.append(new_element)
        else:
            print("Osiągnięto limit pozycji w zamówieniu")

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self.order_elements) != len(other.order_elements):
            return False

        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False
        return True

    def tax_for_order_element(self, order_element):
        product_category = order_element.product.category_name
        if product_category in Order.TAX_RATES:
            tax_rate = Order.TAX_RATES[product_category]
        else:
            tax_rate = Order.BASE_TAX_RATE
        return tax_rate * order_element.calculate_price()

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        product_details = "Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, mark_line])
        return result

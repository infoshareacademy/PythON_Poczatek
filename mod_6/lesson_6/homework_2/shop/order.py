from shop.discount_policy import DiscountPolicy
from shop.errors import ElementsInOrderLimitError
from shop.order_element import OrderElement
from shop.store import Store


class Order:
    MAX_ELEMENTS = 5

    def __init__(self, client_first_name, client_last_name, order_elements=None, discount_policy=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements

        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price)

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) > Order.MAX_ELEMENTS:
            raise ElementsInOrderLimitError(
                allowed_limit=Order.MAX_ELEMENTS,
                message=f"Zamówienie ma limit - {Order.MAX_ELEMENTS} pozycji"
            )
        self._order_elements = value

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) >= Order.MAX_ELEMENTS:
            raise ElementsInOrderLimitError(allowed_limit=Order.MAX_ELEMENTS)

        Store.reserve_product(product, quantity)
        new_element = OrderElement(product, quantity)
        self._order_elements.append(new_element)

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

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        product_details = "Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, mark_line])
        return result

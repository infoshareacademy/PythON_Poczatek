
class ElementsInOrderLimitError(Exception):

    def __init__(self, allowed_limit, message="Przekroczono limit pozycji w zamówieniu", *args):
        self.allowed_limit = allowed_limit
        super().__init__(message, *args)


class ProductNotAvailable(Exception):

    def __init__(self, product_name, *args):
        self.product_name = product_name
        super().__init__(*args)


class TemporaryOutOfStock(ProductNotAvailable):

    def __init__(self, product_name, available_quantity, *args):
        self.available_quantity = available_quantity
        super().__init__(product_name, *args)


class NotValidInput(Exception):
    pass

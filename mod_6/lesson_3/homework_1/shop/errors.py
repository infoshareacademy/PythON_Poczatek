
class ElementsInOrderLimitError(Exception):

    def __init__(self, allowed_limit, message="Przekroczono limit pozycji w zamówieniu", *args):
        self.allowed_limit = allowed_limit
        super().__init__(message, *args)

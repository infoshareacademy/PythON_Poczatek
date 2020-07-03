
# Zaimplementuj metodę __str__ dla klas Order, OrderElement oraz Product (zastępując dotychczasową print_self)

from shop.order import generate_order


def run_homework():
    first_order = generate_order()
    print(first_order)
    second_order = generate_order()
    print(second_order)


if __name__ == '__main__':
    run_homework()


def run_example():
    # shopping_list = ["woda", "chleb", "mąka"]
    # my_list = shopping_list
    # your_list = shopping_list
    #
    # print("shopping_list:", shopping_list)
    # print("my_list:", my_list)
    # print("your_list:", your_list)
    #
    # # Za pomocą funkcji wbudowanej id możemy sprawdzić jaki jest adres w pamięci danego obiektu
    # # (w implementacji CPython)
    # print(id(shopping_list))
    # print(id(my_list))
    # print(id(your_list))
    #
    # print()
    # print("Dodaję ciastka do swojej listy...")
    # my_list.append("ciastka")
    #
    # print("shopping_list:", shopping_list)
    # print("my_list:", my_list)
    # print("your_list:", your_list)
    #
    # print(id(shopping_list))
    # print(id(my_list))
    # print(id(your_list))

    hello_str = "Hello"
    my_str = hello_str
    your_str = hello_str

    print("hello_str:", hello_str)
    print("my_str:", my_str)
    print("your_str:", your_str)

    print(id(hello_str))
    print(id(my_str))
    print(id(your_str))

    print()
    print("Zmieniam swoje przywitanie...")
    my_str += " World!"

    print("hello_str:", hello_str)
    print("my_str:", my_str)
    print("your_str:", your_str)

    print(id(hello_str))
    print(id(my_str))
    print(id(your_str))


if __name__ == '__main__':
    run_example()
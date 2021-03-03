def func_with_different_return_value():
    return 'first', 1.0, False


def func_with_same_return_value():
    return 'first', 'second', 'third'


if __name__ == '__main__':
    # bind_func = True
    # first, second, third = func_with_different_return_value() if bind_func else 'one', 2.0, True
    # print(first, second, third)
    #
    # bind_func = False
    # first, second, third = func_with_different_return_value() if bind_func else 'one', 2.0, True
    # print(first, second, third)

    bind_func = False
    first_2, second_2, third_2 = func_with_same_return_value() if bind_func else 'one', 'two', 'three'
    print(first_2, second_2, third_2)

    bind_func = True
    first_2, second_2, third_2 = func_with_same_return_value() if bind_func else 'one', 'two', 'three'
    print(first_2, second_2, third_2)

    if bind_func:
        first_2, second_2, third_2 = func_with_same_return_value()
    else:
        first_2, second_2, third_2 = 'one', 'two', 'three'

    print(first_2, second_2, third_2)

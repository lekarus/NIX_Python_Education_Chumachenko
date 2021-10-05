def factorial(number):
    """
    The function calculates the factorial of a number

    :param number: input number
    :return: factorial of a number
    """
    if number < 0:
        print('negative numbers cannot calculate the factorial')
    tmp = 1
    for i in range(1, number):
        tmp = tmp * (i + 1)
    return tmp


print(factorial(-10))

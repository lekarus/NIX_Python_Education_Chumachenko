"""
Module for working with calc
"""
from os import system
from calc import Calc


def main_menu():
    """
    method for nice menu display

    :return:
    """
    system('clear')
    print('1. add')
    print('2. minus')
    print('3. multi')
    print('4. division')
    print('5. history')
    print('6. exit')
    print('Choose operation:', end=' ')


calculator = Calc()
while True:
    main_menu()
    CHOSEN = input()
    numbers = []
    if int(CHOSEN) in (1, 2, 3, 4):
        print('enter numbers:')
        while True:
            buf = input()
            if buf == '':
                break
            numbers.append(buf)
        if int(CHOSEN) == 1:
            print(f'addition of this numbers:{numbers} = {calculator.addition(numbers)}')
        if int(CHOSEN) == 2:
            print(f'subtraction of this numbers:{numbers} = {calculator.subtraction(numbers)}')
        if int(CHOSEN) == 3:
            print(f'multiplication of this numbers:{numbers} = '
                  f'{calculator.multiplication(numbers)}')
        if int(CHOSEN) == 4:
            print(f'division of this numbers:{numbers} = {calculator.division(numbers)}')
        while True:
            print('do you want continue?[y/n]', end='')
            tmp = input()
            if tmp.lower() == 'y':
                break
            if tmp.lower() == 'n':
                CHOSEN = 6
                break
    if int(CHOSEN) == 5:
        print(f'History your operations:{calculator.get_operation_history()}')
        while True:
            print('do you want continue?[y/n]', end='')
            tmp = input()
            if tmp.lower() == 'y':
                break
            if tmp.lower() == 'n':
                CHOSEN = 6
                break
    if int(CHOSEN) == 6:
        print('bye')
        break

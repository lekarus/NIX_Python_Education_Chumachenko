"""
module for working with numbers
"""


class Calc:
    """
    Class allowing make some calculate
    """

    def __init__(self):
        self.operation_history = []

    def addition(self, numbers):
        """
        function for adding arguments and returning the sum
        """
        res = 0
        try:
            for number in numbers:
                res += int(number)
            self.operation_history.append(f'addition: {str(res)}')
            return res
        except TypeError:
            return 'TypeError'

    def subtraction(self, numbers):
        """
        function for subtracting arguments starting with your 1 arg. and returning the difference
        """
        try:
            res = int(numbers[0])
            for number in numbers[1:]:
                res -= int(number)
            self.operation_history.append(f'subtraction: {str(res)}')
            return res
        except TypeError:
            return 'TypeError'

    def multiplication(self, numbers):
        """
        function for multiplication arguments and returning the product
        """
        res = 1
        try:
            for number in numbers:
                res *= int(number)
            self.operation_history.append(f'multiplication: {str(res)}')
            return res
        except TypeError:
            return 'TypeError'

    def division(self, numbers):
        """
        function for division arguments starting from 1 and returning the quotient
        """
        try:
            res = int(numbers[0])
            for number in numbers[1:]:
                res /= int(number)
            self.operation_history.append(f'division: {str(res)}')
            return res
        except TypeError:
            return 'TypeError'
        except ZeroDivisionError:
            return 'Division by zero'

    def get_operation_history(self):
        """
        Method for check operation history
        """
        return self.operation_history

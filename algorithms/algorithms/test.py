"""module for testing algorithms: binary search, quick sort, factorial
"""
from random import randint
import pytest
from main import binary_search, quick_sort, factorial


def create_mas(mas_sort):
    """method for creating 10 arrays
    :param mas_sort: boolean expression whether or not to sort arrays
    :return: 10 arrays
    """
    tuples = []
    for i in range(10):
        buf_tuple = (random_mas(mas_sort), )
        tuples.append(buf_tuple)
    return tuples


def random_mas(mas_sort):
    """method for creating random array
    :param mas_sort: boolean expression whether or not to sort arrays
    :return: random array
    """
    buf_mas = []
    for i in range(randint(2, randint(2, 10))):
        buf_int = randint(-100, 100)
        while not buf_mas.count(buf_int) != 1:
            buf_int = randint(-100, 100)
        buf_mas.append(buf_int)
    if mas_sort:
        buf_mas.sort()
    return buf_mas


@pytest.mark.parametrize("mas", create_mas(True))
def test_binary_search(mas):
    """method for testing binary search
    """
    value = mas[0][randint(0, len(mas)-1)]
    assert binary_search(mas[0], value) == mas[0].index(value)


@pytest.mark.parametrize("mas", create_mas(False))
def test_quick_sort(mas):
    """method for testing quick sort
    """
    test_mas = mas[0]
    quick_sort(test_mas)
    mas[0].sort()
    assert test_mas == mas[0]


@pytest.mark.parametrize("number, fact", [(0, 1), (1, 1), (2, 2), (3, 6),
                                          (4, 24), (5, 120), (6, 720)])
def test_factorial(number, fact):
    """method for testing factorial
    """
    assert factorial(number) == fact

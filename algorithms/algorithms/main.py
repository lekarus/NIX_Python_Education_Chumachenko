"""Module for work with binary search and quick sort
"""


def binary_search(mas, value):
    """Method for finding an item in a sorted array by binary search

        Args:
            mas (list): sorted array
            value: required item

        Returns:
            int: index of value
    """
    i = 0
    index = int(len(mas)/2)
    if index > 2:
        step = int(index/2)
    else:
        step = 1
    while i < len(mas):
        if mas[index] == value:
            return index
        if mas[index] < value:
            index = index + step
        else:
            index = index - step
        if step != 1:
            step = int(step/2)
        else:
            step = 1
        i += 1
    return None


def quick_sort(mas):
    print(mas)
    """"method for sorting an array by quicksort

        Args:
            mas (list): unsorted array
    """
    stack = [(0, len(mas)-1)]
    while stack:
        start, end = stack.pop()
        if end <= start:
            continue
        i = part_sort(mas, start, end)
        if i - start > end - i:
            stack.append((start, i - 1))
            stack.append((i+1, end))
        else:
            stack.append((i + 1, end))
            stack.append((start, i - 1))


def part_sort(mas, start, end):
    """method for sorting part of array relative to the pivot

        Args:
            mas (list): unsorted array
            start (int): start index
            end (int): end index

        Returns:
            (int): pivot index
    """
    pivot = mas[int((start+end)/2)]
    i = start
    j = end
    while i <= j:
        while mas[i] < pivot:
            i += 1
        while mas[j] > pivot:
            j -= 1
        if i >= j:
            break
        mas[i], mas[j] = mas[j], mas[i]
    return i


def factorial(numb):
    """method for calculate factorial for a number

        Args:
            numb (int): number

        Returns:
            (int) : factorial number
    """
    if numb in (0, 1):
        return 1
    return numb * factorial(numb - 1)

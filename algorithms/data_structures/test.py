"""module for testing data structures
"""
from random import randint
import pytest
from main import LinkedList, Queue, Stack, HashTable, BinaryTree, Graph


def create_mas(numb):
    """method for creating random arrays

        Args:
            numb (int): array dimension

        Returns:
            (list): random array
    """
    mas = []
    for i in range(numb):
        mas.append(randint(-100, 100))
    return mas


@pytest.mark.parametrize("mas", [(create_mas(5)), (create_mas(5)), (create_mas(5)), (create_mas(5)),
                                 (create_mas(5))])
def test_linked_list(mas):
    """method for testing linked list
    :param mas: input array
    """
    l_list = LinkedList(*mas)
    l_list.append(0)
    mas.append(0)
    for i, j in zip(l_list, mas):
        assert i == j


@pytest.mark.parametrize("mas", [(create_mas(5)), (create_mas(5)), (create_mas(5)), (create_mas(5)),
                                 (create_mas(5))])
def test_queue(mas):
    """method for testing queue
    :param mas: input array
    """
    queue = Queue(*mas)
    queue.enqueue(0)
    mas.append(0)
    for i, j in zip(queue, mas):
        assert i == j


@pytest.mark.parametrize("mas", [(create_mas(5)), (create_mas(5)), (create_mas(5)), (create_mas(5)),
                                 (create_mas(5))])
def test_stack(mas):
    """method for testing stack
    :param mas: input array
    """
    stack = Stack(*mas)
    stack.push(0)
    mas = [0, *mas]
    for i, j in zip(stack, mas):
        assert i == j


@pytest.mark.parametrize("key, mas", [(['orange', 'banana', 'apple'], create_mas(3)),
                                 (['red', 'blue', 'green'], create_mas(3)),
                                 (['one', 'two', 'three'], create_mas(3))])
def test_hash(key, mas):
    """method for testing hash table
    :param key: input keys
    :param mas: input values
    """
    dictionary = {str(key[0]): mas[0], str(key[1]): mas[1], str(key[1]): mas[1]}
    hash_table = HashTable(key[0], mas[0])
    hash_table.insert(key[1], mas[1])
    hash_table.insert(key[2], mas[2])
    for i, j in zip(hash_table, dictionary):
        assert i.get_value() == dictionary.get(j)


@pytest.mark.parametrize("mas", [(create_mas(5)), (create_mas(5)), (create_mas(5))])
def test_binary(mas):
    """method for testing binary tree
    :param mas: input array
    """
    binary_tree = BinaryTree(*mas)
    if mas[1] > mas[0]:
        assert binary_tree.head.get_more().get_value() == mas[1]
    else:
        assert binary_tree.head.get_less().get_value() == mas[1]


@pytest.mark.parametrize("mas", [(create_mas(5)), (create_mas(5)), (create_mas(5))])
def test_graph(mas):
    """method for testing graph
    :param mas: input array
    """
    graph = Graph(mas[0])
    counter = 1
    while counter <= len(mas)-2:
        graph.insert(mas[counter])
        counter += 1
    graph.insert(mas[counter], *mas[:counter])
    for node, i in zip(graph.lookup(mas[counter]).get_conn(), mas[:-1]):
        assert node.get_value() == i

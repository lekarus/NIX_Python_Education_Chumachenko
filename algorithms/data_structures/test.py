"""module for testing data structures
"""
import pytest
from main import LinkedList, Queue, Stack, HashTable, BinaryTree, Graph


@pytest.fixture()
def linked_fixture():
    """fixture for testing linked list"""
    l_list = LinkedList(5, 10, 15, 25, 30)
    l_list.insert(3, 20)
    l_list.delete(4)
    return l_list


@pytest.fixture()
def queue_fixture():
    """fixture for testing queue"""
    queue = Queue(5, 10, 15, 20, 25)
    queue.dequeue()
    queue.enqueue(30)
    return queue


@pytest.fixture()
def stack_fixture():
    """fixture for testing stack"""
    stack = Stack(5, 10, 15, 20)
    stack.pop()
    stack.push(25)
    return stack


@pytest.fixture()
def hash_fixture():
    """fixture for testing hash table"""
    hash_table = HashTable('apple', 10)
    hash_table.insert('banana', 20)
    hash_table.insert('orange', 30)
    hash_table.delete('orange')
    return hash_table


@pytest.fixture()
def binary_tree_fixture():
    """fixture for testing binary tree"""
    binary_tree = BinaryTree(50, 75, 30, 90, 20, 60, 40, 35, 45)
    binary_tree.delete(30)
    return binary_tree


@pytest.fixture()
def graph_fixture():
    """fixture for testing graph"""
    graph = Graph(10)
    graph.insert(15, 10)
    graph.insert(25, 10, 15)
    graph.delete(10)
    return graph


def test_list(linked_fixture):
    """method for testing linked list"""
    assert linked_fixture.lookup(20) == 3
    assert linked_fixture.lookup(30) == 4


def test_queue(queue_fixture):
    """method for testing queue"""
    assert queue_fixture.peek() == 10


def test_stack(stack_fixture):
    """method for testing stack"""
    assert stack_fixture.peek() == 25


def test_hash(hash_fixture):
    """method for testing hash table"""
    assert hash_fixture.lookup('apple') == 10
    assert hash_fixture.lookup('banana') == 20
    assert hash_fixture.lookup('orange') is None


def test_binary(binary_tree_fixture):
    """method for testing binary tree"""
    assert binary_tree_fixture.lookup(50) == binary_tree_fixture.head
    assert binary_tree_fixture.lookup(75) == binary_tree_fixture.head.get_more()


def test_graph(graph_fixture):
    """method for testing graph"""
    assert graph_fixture.lookup(10) is None
    assert graph_fixture.lookup(15) == graph_fixture.lookup(25).get_conn().head.get_value()

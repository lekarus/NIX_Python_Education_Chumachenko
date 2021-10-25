"""Module for work with some data structures
"""
import hashlib


class ListNode:
    """A class that implements a linked items

    Args:
        value: node value
    """
    def __init__(self, value):
        self._value = value
        self._next = None

    def get_value(self):
        """Getter for value

            Returns:
                value: value
        """
        return self._value

    def set_value(self, value):
        """Setter for value

            Args:
                value: new value
        """
        self._value = value

    def get_next(self):
        """Getter for next item

            Returns:
                next: next item
        """
        return self._next

    def set_next(self, next_par):
        """Setter for next

            Args:
                next_par: new reference for next item
        """
        self._next = next_par

    def __str__(self):
        return str(self._value)


class HashNode(ListNode):
    """A class that implements linked items with a key

    Args:
        key: node key
        value: node value
    """
    def __init__(self, key, value):
        super().__init__(value)
        self._key = key
        self._hashkey = hashlib.md5(key.encode()).hexdigest()

    def get_key(self):
        """Getter for key

            Returns:
                key: key
        """
        return self._key

    def get_hashkey(self):
        """Getter for hashkey

            Returns:
                hashkey: encryption key value
        """
        return self._hashkey


class BinaryNode:
    """A class that implements the nodes of a binary tree

    Args:
        value: node value
    """
    def __init__(self, value):
        self._more = None
        self._less = None
        self._value = value

    def get_value(self):
        """Getter for value

            Returns:
                value: value
        """
        return self._value

    def set_value(self, value):
        """Setter for value

            Args:
                value: new value
        """
        self._value = value

    def get_more(self):
        """Getter for more mode

            Returns:
                more: reference to more node
        """
        return self._more

    def set_more(self, more):
        """Setter for more node

            Args:
                more: new reference to more node
        """
        self._more = more

    def get_less(self):
        """Getter for less node

            Returns:
                less: reference to less node
        """
        return self._less

    def set_less(self, less):
        """Setter for less node

            Args:
                less: new reference to less node
        """
        self._less = less


class GraphNode:
    """A class that implements the nodes of a graph

    Args:
        value: node value
    """
    def __init__(self, value):
        self._value = value
        self._conn = None

    def get_value(self):
        """Getter for value

            Returns:
                value: value
        """
        return self._value

    def set_value(self, value):
        """Setter for value

            Args:
                value: new value
        """
        self._value = value

    def get_conn(self):
        """Getter for connections

            Returns:
                conn: netlist
        """
        return self._conn

    def set_conn(self, conn):
        """Setter for connections

            Args:
                conn: netlist
        """
        self._conn = conn


class LinkedList:
    """A class that implements a single linked list

    Args:
        values: node values
    """
    def __init__(self, *values):
        tmp_node = ListNode(values[0])
        self.head = tmp_node
        self.tail = tmp_node
        self.cur = self.head
        self.head.next = self.tail
        self.length = 1
        for list_value in values[1:]:
            self.append(list_value)

    def prepend(self, value):
        """A method for adding an item to the begining of the linked list

        Args:
            value: node value
        """
        tmp_node = ListNode(value)
        tmp_node.next = self.head
        self.head = tmp_node
        self.length += 1

    def append(self, value):
        """A method for adding an item to the end of the linked list

        Args:
            value: node value
        """
        tmp_node = ListNode(value)
        self.tail.set_next(tmp_node)
        self.tail = tmp_node
        self.length += 1

    def lookup(self, value):
        """A method which returns the index of the list item

        Args:
            value: node value

        Returns:
            int: index of the item
        """
        tmp = self.head
        index = 0
        while tmp is not None:
            if tmp.get_value() == value:
                return index
            tmp = tmp.get_next()
            index += 1

    def insert(self, index, value):
        """A method for adding an item to the desired position with the shift of the items
        to the right

        Args:
            index (int): the position at which to insert the item
            value: node value
        """
        tmp = self.head
        counter = 0
        while counter < index - 1:
            tmp = tmp.get_next()
            counter += 1
        tmp_node = ListNode(value)
        tmp_node.set_next(tmp.get_next())
        tmp.set_next(tmp_node)
        self.length += 1

    def delete(self, index):
        """A method for removing an item by its index

        Args:
            index (int): the position of the item to removing
        """
        if index == 0:
            self.head = self.head.get_next()
            self.cur = self.head
        if index == self.length - 1:
            self.tail = self.head
        tmp = self.head
        counter = 0
        while counter < index-1:
            tmp = tmp.get_next()
            counter += 1
        tmp.set_next(tmp.get_next().get_next())
        self.length -= 1

    def remove(self, value):
        """A method for removing an item by its value

        Args:
            value: the value of the item to removing
        """
        tmp_node = self.head
        if self.head.get_value() == value:
            self.head = self.head.get_next()
            self.cur = self.head
        counter = 0
        while counter < self.length - 1:
            if tmp_node.get_next().get_value() == value:
                tmp_node.set_next(tmp_node.get_next())
                break
            tmp_node = tmp_node.get_next()
            counter += 1

    def contain(self, value):
        """A method that checks the list for an item

        Args:
            value: the value of the item you are looking for
        """
        tmp = self.head
        counter = 0
        while counter < self.length:
            if value == tmp.get_value():
                return True
            tmp = tmp.next
            counter += 1
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        tmp = self.cur
        self.cur = self.cur.get_next()
        if self.cur == self.head:
            self.cur = None
        return tmp.get_value()

    def __len__(self):
        return self.length


class Queue:
    """A class that implements a queue

    Args:
        values: node values
    """
    def __init__(self, *values):
        tmp_node = ListNode(values[0])
        self.head = tmp_node
        self.tail = tmp_node
        self.cur = self.head
        self.head.set_next(self.tail)
        for queue_value in values[1:]:
            self.enqueue(queue_value)

    def enqueue(self, value):
        """A method for adding an item to the end of the queue

        Args:
            value: node value
        """
        tmp_node = ListNode(value)
        self.tail.set_next(tmp_node)
        self.tail = tmp_node

    def dequeue(self):
        """A method for removing an item from the end of the queue
        """
        self.head = self.head.get_next()
        self.cur = self.head

    def peek(self):
        """A method to view the first item in queue

        Returns:
            value: first item in queue
        """
        return self.head.get_value()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        tmp = self.cur
        self.cur = self.cur.get_next()
        return tmp.get_value()


class Stack:
    """A class that implements a stack

    Args:
        values: node values
    """
    def __init__(self, *values):
        tmp_node = ListNode(values[-1])
        self.head = tmp_node
        self.cur = self.head
        for stack_value in values[-2::-1]:
            self.push(stack_value)

    def push(self, value):
        """A method for adding an item to the begining of the stack

        Args:
            value: node value
        """
        tmp_node = ListNode(value)
        tmp_node.set_next(self.head)
        self.head = tmp_node
        self.cur = self.head

    def pop(self):
        """A method for removing an item from the begining of the stack
        """
        self.head = self.head.get_next()
        self.cur = self.head

    def peek(self):
        """A method to view the first item in stack

        Returns:
            value: first item in stack
        """
        return self.head.get_value()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        tmp = self.cur
        self.cur = self.cur.get_next()
        return tmp.get_value()


class HashTable:
    """A class that implements a hash table

    Args:
        key: node key
        value: node value
    """
    def __init__(self, key, value):
        tmp_node = HashNode(key, value)
        self.head = tmp_node
        self.tail = tmp_node
        self.cur = self.head
        self.head.set_next(self.tail)

    def insert(self, key, value):
        """A method for adding an item to the table by key

        Args:
            key: node key
            value: node value
        """
        tmp_node = HashNode(key, value)
        self.tail.set_next(tmp_node)
        self.tail = tmp_node

    def lookup(self, key):
        """A method to view an item by key

        Args:
            key: the key of the item to be looking for

        Returns:
            value: value by key
        """
        tmp = self.head
        while tmp is not None:
            if tmp.get_hashkey() == hashlib.md5(key.encode()).hexdigest():
                return tmp.get_value()
            tmp = tmp.get_next()
        return None

    def delete(self, key):
        """A method for deleting an item by key

        Args:
            key: the key of the item to remove
        """
        tmp = self.head
        prev_tmp = tmp
        while tmp is not None:
            if tmp.get_hashkey() == hashlib.md5(key.encode()).hexdigest():
                prev_tmp.set_next(tmp.get_next())
                break
            prev_tmp = tmp
            tmp = tmp.get_next()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        if self.cur is None:
            raise StopIteration
        tmp = self.cur
        self.cur = self.cur.get_next()
        return tmp


class BinaryTree:
    """A class that implements a binary search tree

    Args:
        values: node values
    """
    def __init__(self, *values):
        tmp_node = BinaryNode(values[0])
        self.head = tmp_node
        for binary_value in values[1:]:
            self.insert(binary_value)

    def insert(self, value, cur=None):
        """A method for adding an item to the binary tree

        Args:
            value: node value
            cur (optional): the current node of the binary tree
                Defaults to None
        """
        if cur is None:
            cur = self.head
        if value > cur.get_value():
            if cur.get_more() is not None:
                self.insert(value, cur=cur.get_more())
            else:
                cur.set_more(BinaryNode(value))
        else:
            if cur.get_less() is not None:
                self.insert(value, cur=cur.get_less())
            else:
                cur.set_less(BinaryNode(value))

    def lookup(self, value, cur='head'):
        """A method to view an item by binary tree

        Args:
            value: node value
            cur (optional): the current node of the binary tree
                Defaults to None

        Returns:
            value: reference to the desired node
        """
        if cur == 'head':
            cur = self.head
        if value > cur.get_value():
            return self.lookup(value, cur=cur.get_more())
        if value < cur.get_value():
            return self.lookup(value, cur=cur.get_less())
        return cur

    def delete(self, value):
        """Method for deleting node from binary tree

            Args:
                value: node value
        """
        delete_node = self.lookup(value)
        parent_node = self._find_par(value)
        if delete_node.get_more() is None and delete_node.get_less() is None:
            if parent_node is None:
                self.head = None
            else:
                return (parent_node.set_less(None)
                    if value < parent_node.get_value()
                    else parent_node.set_more(None))
        elif delete_node.get_more() is None:
            if parent_node is None:
                self.head = delete_node.get_less()
            else:
                return (parent_node.set_less(delete_node.get_less())
                    if value < parent_node.get_value()
                    else parent_node.set_more(delete_node.get_less()))
        elif delete_node.get_less() is None:
            if parent_node is None:
                self.head = delete_node.get_more()
            else:
                return (parent_node.set_less(delete_node.get_more())
                    if value < parent_node.get_value()
                    else parent_node.set_more(delete_node.get_more()))
        else:
            less_node = self._find_last_less(delete_node.get_more())
            self._find_par(less_node.get_value()).set_less(None)
            if parent_node is None:
                less_node.set_more(self.head.get_more())
                less_node.set_less(self.head.get_less())
                self.head = less_node
            else:
                less_node.set_more(delete_node.get_more())
                less_node.set_less(delete_node.get_less())
                return (parent_node.set_less(less_node)
                    if value < parent_node.get_value()
                    else parent_node.set_more(less_node))
        delete_node.set_less(None)
        delete_node.set_more(None)
        return self.head

    def _find_par(self, value, cur='head'):
        """Method for finding the parent of node

            Args:
                value: node value
                cur: current node
                    Default: 'head'
        """
        if self.head.get_value() == value:
            return None
        if cur == 'head':
            cur = self.head
        if value == cur.get_more().get_value():
            return cur
        if value == cur.get_less().get_value():
            return cur

        if value > cur.get_value():
            return self._find_par(value, cur.get_more())
        if value < cur.get_value():
            return self._find_par(value, cur.get_less())
        return None

    def _find_last_less(self, node):
        """Method for finding the last less node from binary tree
            Args:
                value: cur
                cur: current node
                    Default: 'head'
        """
        if node.get_less() is None:
            return node
        return self._find_last_less(node.get_less())


class Graph:
    """A class that implements a graph

    Args:
        value: node value
    """
    def __init__(self, value):
        self.nodes = LinkedList(GraphNode(value))

    def insert(self, value, *conn):
        """A method for adding an item to the graph

        Args:
            value: node value
            *conn (optional): references to other nodes
        """
        self.nodes.append(GraphNode(value))
        for i in self.nodes:
            if i.get_value() in conn:
                if self.nodes.tail.get_value().get_conn() is None:
                    self.nodes.tail.get_value().set_conn(LinkedList(i))
                else:
                    self.nodes.tail.get_value().get_conn().append(i)
                if i.get_conn() is None:
                    i.set_conn(LinkedList(self.nodes.tail.get_value()))
                else:
                    i.get_conn().append(self.nodes.tail.get_value())
        self.nodes.cur = self.nodes.head

    def lookup(self, value):
        """A method for adding an item to the graph

        Args:
            value: node value
            *conn (optional): references to other nodes

        Returns:
            value: reference to the desired node
        """
        for i in self.nodes:
            if i.get_value() == value:
                self.nodes.cur = self.nodes.head
                return i
        self.nodes.cur = self.nodes.head
        return None

    def delete(self, value):
        """A method for removing an item bfrom a graph

        Args:
            value: node value
        """
        tmp_node = None
        for i in self.nodes:
            if value == i.get_value():
                tmp_node = i
                self.nodes.remove(tmp_node)
                break
        self.nodes.cur = self.nodes.head

        for i in self.nodes:
            if i.get_conn().contain(tmp_node):
                i.get_conn().remove(tmp_node)
        self.nodes.cur = self.nodes.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.nodes.cur is None:
            raise StopIteration
        tmp = self.nodes.cur
        self.nodes.cur = self.nodes.cur.get_next()
        if self.nodes.cur == self.nodes.head:
            self.nodes.cur = None
        return tmp.get_value()


b = BinaryTree()
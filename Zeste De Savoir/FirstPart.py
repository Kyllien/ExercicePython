class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Deque:
    def __init__(self, iterable=()):
        self.first = None # Premier maillon
        self.last = None # Dernier maillon
        for element in iterable:
            self.append(element)

    def __iter__(self):
        return DequeIterator(self)

    def append(self, value):
        node = Node(value, None)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = node

    def get_node(self, n):
        node = self.first
        while n > 0 and node is not None:
            node = node.next
            n -= 1
        if node is None:
            raise IndexError("list index out of range")
        return node

    def insert(self, i, value):
        if not i:
            node = Node(value, next=self.first)
            self.first = node
        else:
            prev = self.get_node(i - 1)
            node = Node(value, prev.next)
        prev.next = node
        if node.next is None:
            self.last = node

    def __len__(self):
        node = self.first
        size = 0
        while node is not None:
            node = node.next
            size += 1
        return size

    def __getitem__(self, key):
        if isinstance(key, slice):
            new_list = Deque()
            indices = range(*key.indices(len(self)))
            for i in indices:
                new_list.append(self[i])
            return new_list
        else:
            return self.get_node(key).value

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            indices = range(*key.indices(len(self)))
            for i, v in zip(indices, value):
                self[i] = v
        else:
            self.get_node(key).value = value

    def __contains__(self, value):
        node = self.first
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

class DequeIterator:
    def __init__(self, deque):
        self.current = deque.first

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

    def __iter__(self):
        return self

    def __eq__(self, other):
        if not isinstance(other, Deque):
            return NotImplemented
        if len(self) != len(other):
            return False
        for elem1, elem2 in zip(self, other):
            if elem1 != elem2:
                return False
        return True


for i in Deque([1, 2, 3, 4, 5]):
    print(i)

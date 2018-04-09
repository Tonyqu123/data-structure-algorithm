# 用list实现，push和pop的平均复杂度为O(n)
class Stack:
    """ Stack ADT, using a python list
    Stack()
    isEmpty()
    length()
    pop(): assert not empty
    peek(): assert not empty, return top of non-empty stack without removing it
    push(item)
    """
    def __init__(self):
        self._items = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def peek(self):
        assert not self.isEmpty()
        return self._items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self._items.pop()

    def push(self, item):
        self._items.append(item)


class Stack:
    """ Stack ADT, use linked list
    使用list实现很简单，但是如果涉及大量push操作，list的空间不够时复杂度退化到O(n)
    而linked list可以保证最坏情况下仍是O(1)
    """
    def __init__(self):
        self._top = None    # top节点, _StackNode or None
        self._size = 0    # int

    def isEmpty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        assert not self.isEmpty()
        return self._top.item

    def pop(self):
        assert not self.isEmpty()
        node = self._top
        self.top = self._top.next
        self._size -= 1
        return node.item

    def _push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1


class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link
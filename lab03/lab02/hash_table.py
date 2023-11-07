class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.elements = [None] * size

    def _hash(self, value):
        return hash(value) % self.size

    def insert(self, value):
        index = self._hash(value)
        position = 0
        if not self.elements[index]:
            self.elements[index] = ListNode(value)
        else:
            node = self.elements[index]
            while node.next:
                position += 1
                node = node.next
            node.next = ListNode(value)
            position += 1
        return index, position

    def search(self, value):
        index = self._hash(value)
        node = self.elements[index]
        while node:
            if node.value == value:
                return index
            node = node.next
        return None

    def delete(self, value):
        index = self._hash(value)
        node = self.elements[index]
        prev = None

        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.elements[index] = node.next
                return True
            prev, node = node, node.next
        return False

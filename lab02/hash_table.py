class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [None] * size

    def _hash(self, value):
        return hash(value) % self.size

    def insert(self, value):
        index = self._hash(value)
        if not self.table[index]:
            self.table[index] = ListNode(value)
        else:
            node = ListNode(value)
            node.next = self.table[index]
            self.table[index] = node

    def search(self, value):
        index = self._hash(value)
        node = self.table[index]
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def delete(self, value):
        index = self._hash(value)
        node = self.table[index]
        prev = None

        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return True
            prev, node = node, node.next
        return False

from lab02.hash_table import HashTable

class SymbolTable:
    def __init__(self):
        self.table = HashTable(size=100)
      
    def insert(self, value):
        return self.table.insert(value)

    def search(self, value):
        return self.table.search(value)
    
    def delete(self, value):
        return self.table.delete(value)
    
    def hash(self, value):
        return self.table._hash(value)
    
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table.elements):
            if bucket:
                node = bucket
                while node:
                    result.append(f"Index {i}: {node.value}")
                    node = node.next
        return "\n".join(result)



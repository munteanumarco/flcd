from hash_table import HashTable

class SymbolTable:
    def __init__(self):
        self.table = HashTable(size=100)
      
    def insert(self, value):
        self.table.insert(value)

    def search(self, value):
        return self.table.search(value)
    
    def delete(self, value):
        return self.table.delete(value)


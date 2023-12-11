#Write a program to implement a hash table.
print ("\nSubi - Day 83 of #100DaysOfCode\n") 
print("\nWrite a program to implement a hash table\n")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
            
hash_table = HashTable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")

print(hash_table.search("key1"))  
print(hash_table.search("key2")) 

hash_table.delete("key1")

print(hash_table.search("key1"))
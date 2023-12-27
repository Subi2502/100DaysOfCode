#Write a program to implement a hash map.
print ("\nSubi - Day 99 of #100DaysOfCode\n") 
print("\nWrite a program to implement a hash map\n")

class HashMap(object):
    def __init__(self, size):

        self.data = [[]] * (size)

    def _hash(self, key):

        hash_value = 0

        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)

        return hash_value

    def set(self, key, value):

        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):

        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:

            for i in range(len(currentBucket)):

                if currentBucket[i][0] == key:

                    return currentBucket[i][1]

        return "Data Not Found"

    def __str__(self):
        return "".join(str(item) for item in self.data)

myHash = HashMap(50)

myHash.set("arun", 946)
myHash.set("joe", 465)
myHash.set("ruby", 432)

print(myHash)

print(myHash.get("ruby"))  
print(myHash.get("sam"))  
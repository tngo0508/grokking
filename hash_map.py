from bucket import *


class MyHashMap():
    # Use the constructor below to initialize the 
    # hash map based on the keyspace
    def __init__(self, key_space):
        self.bucket = [[]] * key_space
        self.k = key_space

    def put(self, key, value):
        hash_value = key % self.k
        while hash_value > self.k:
            hash_value %= self.k
        
        self.bucket[hash_value] = value

    def get(self, key):
        hash_value = key % self.k
        while hash_value > self.k:
            hash_value %= self.k
        return self.bucket[hash_value] if self.bucket[hash_value] else -1

    def remove(self, key):
        hash_value = key % self.k
        while hash_value > self.k:
            hash_value %= self.k
        self.bucket[hash_value] = []

## feedback

class MyHashMap:
    def __init__(self, key_space):
        self.bucket = [[] for _ in range(key_space)]
        self.k = key_space

    def put(self, key, value):
        hash_value = key % self.k
        self.bucket[hash_value] = value

    def get(self, key):
        hash_value = key % self.k
        return self.bucket[hash_value] if self.bucket[hash_value] else None

    def remove(self, key):
        hash_value = key % self.k
        self.bucket[hash_value] = None


# solution
# A class implementation of the bucket data structure
class Bucket:
    # Initialize bucket here
    def __init__(self):
        self.bucket = []

    # get value from bucket
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    # put value in bucket
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    # delete value from bucket
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


from bucket import *


class MyHashMap():
    # Initialize hash map here
    def __init__(self, key_space):
        # It’s better to have a prime number, so there's less collision
        self.key_space = key_space
        self.buckets = [Bucket()] * self.key_space

    # Function to add value of a given key
    # hash map at the relevant hash address
    def put(self, key, value):
        if key== None or value == None:
            return
            
        hash_key = key % self.key_space
        self.buckets[hash_key].update(key, value)

    # Function to fetch corresponding value of a given key
    def get(self, key):
        if key == None:
            return -1
        hash_key = key % self.key_space
        return self.buckets[hash_key].get(key)

    # Function to remove corresponding value of a given key
    def remove(self, key):
        hash_key = key % self.key_space
        self.buckets[hash_key].remove(key)

# Driver code
def main():
    # Creating a hash map of size 11
    key_space = 11
    input_hash_map = MyHashMap(key_space)
    keys_list = [5, 11, 12, 15, 22, 10]
    funcs = ["Get", "Get", "Put", "Get",
             "Put", "Get", "Get", "Remove",
             "Get", "Get", "Remove", "Get"]
    func_keys = [[5], [15], [15, 250], [15], 
                 [121, 110], [121], [10], [11], [11],
                 [13], [13], [None]]

    for i in range(len(funcs)):
        if funcs[i] == "Put":
            print(
                i + 1,  ".\t put(", func_keys[i][0],  ", ", func_keys[i][1],  ")", sep="")
            if not func_keys[i][0] in keys_list:
                keys_list.append(func_keys[i][0])
            input_hash_map.put(func_keys[i][0], func_keys[i][1])
        elif funcs[i] == "Get":
            print(i + 1, ".\t get(", func_keys[i][0], ")", sep="")
            print("\t Value returned: ", input_hash_map.get(
                func_keys[i][0]), sep="")
        elif funcs[i] == "Remove":
            print(i + 1,  ". \t remove(", func_keys[i][0], ")", sep="")
            input_hash_map.remove(func_keys[i][0])

        print("-"*100)


if __name__ == '__main__':
    main()
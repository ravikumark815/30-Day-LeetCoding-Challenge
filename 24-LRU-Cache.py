'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Author: https://github.com/ravikumark815
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        
    def get(self, key: int) -> int:
        val = -1
        if key in self.values: 
            val =  self.values.pop(key)
            self.values[key] = val
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.pop(key)
            self.values[key] = value
        elif self.capacity > len(self.values):
            self.values[key] = value
        else:
            to_remove = list(self.values.keys())[0]
            self.values.pop(to_remove)
            self.values[key] = value

#!/usr/bin/env python3
'''
LRU caching
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' LRUCache Class '''
    def __init__(self):
        ''' Initializes an instance '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        ''' Add an item in the cache '''
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.queue:
            discard = self.queue.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key '''
        if key in self.cache_data.keys():
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None

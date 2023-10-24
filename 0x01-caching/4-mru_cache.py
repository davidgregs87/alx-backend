#!/usr/bin/env python3
'''
MRU caching
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache Class '''
    def __init__(self):
        ''' Initializes an instance '''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        ''' Add an item in the cache '''
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key '''
        if key in self.stack:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache_data.get(key)
        return None

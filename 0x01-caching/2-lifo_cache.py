#!/usr/bin/env python3
'''
LIFO caching
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache Class '''
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
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key '''
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None

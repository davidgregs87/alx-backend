#!/usr/bin/env python3
'''
Basic Dictionary
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache Class '''
    def __init__(self):
        ''' Initializes an instance '''
        super().__init__()

    def put(self, key, item):
        ''' Add an item in the cache '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key '''
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None

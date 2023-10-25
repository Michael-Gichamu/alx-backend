#!/usr/bin/python3
"""Contains Class FIFOCache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Cache replacement Policy:
    LIFO Algorithm

    Args:
        BaseCaching (Class): Parent Class: Caching System.
    """
    def __init__(self):
        """
        Initialize Parent Class.
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """
        Insert an item to cache storage
        Discard first item if cache is full.

        Args:
            key (any): key.
            item (any): value.
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(self.last_key)
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """
        Get Value

        Args:
            key (any): key.

        Returns:
            Value of the key from cache storage.
        """
        if key in self.cache_data and self.cache_data[key] is not None:
            return self.cache_data[key]
        else:
            return None

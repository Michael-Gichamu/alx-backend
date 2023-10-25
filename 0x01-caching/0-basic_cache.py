#!/usr/bin/python3
"""Contains Class BasicCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching.
    Args:
        BaseCaching (Class): Parent Class: Caching System.
    """
    def __init__(self):
        """
        Initialize Parent Class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Insert an item to cache storage.
        Args:
            key (any): key.
            item (any): value.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get Value
        Args:
            key (any): key.

        Returns:
            Value of the key from cache storage.
        """
        if key in self.cache_data or self.cache_data[key] is not None:
            return self.cache_data[key]
        else:
            return None

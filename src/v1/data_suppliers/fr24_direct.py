#!/usr/bin/python3

"""
f24.data_suppliers.fr24_direct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class handling direct data supply.
"""

import requests
from .cache import Cache


class Fr24Direct:

    HOST_PATH = 'http://www.flightradar24.com/'

    def __init__(self, filename, query=None):
        if query is None:
            print('lol')
        self.uri = '{}{}?{}'.format(self.HOST_PATH, filename, query)

    def get_data(self, bypass=False):
        cache = Cache()
        cache_lookup = cache.lookup(uri=self.uri)
        if cache_lookup is not None and not bypass:
            print('Cache hit')
            jdata = cache_lookup
        else:
            print('Cache miss')
            jdata = requests.get(self.uri).json()
            cache.store(uri=self.uri, data=jdata)
        return jdata

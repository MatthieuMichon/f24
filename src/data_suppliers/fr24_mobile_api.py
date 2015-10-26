#!/usr/bin/python3

"""
f24.data_suppliers.fr24_mobile_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class handling data supply through the mobile API.
"""

import requests
from .cache import Cache


class Fr24MobileApi:

    HOST_PATH = "http://mobile.api.fr24.com/common/v1/"

    def __init__(self, filename, query=None):
        self.uri = self.HOST_PATH + filename + "?" + query

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

#!/usr/bin/python3

"""
f24.data_suppliers.fr24_direct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class handling direct data supply.
"""

import requests


class Fr24Direct:

    HOST_PATH = "http://www.flightradar24.com/"

    def __init__(self, filename, query=None):
        if query is None:
            self.uri = self.HOST_PATH + filename
        else:
            self.uri = self.HOST_PATH + filename + "?" + query

    def get_data(self):
        rdata = requests.get(self.uri)
        jdata = rdata.json()
        return jdata

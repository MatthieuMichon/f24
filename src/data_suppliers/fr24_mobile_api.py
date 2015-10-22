#!/usr/bin/python3

"""
f24.data_suppliers.fr24_mobile_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class handling data supply through the mobile API.
"""

import requests


class Fr24MobileApi:

    HOST_PATH = "http://mobile.api.fr24.com/common/v1/"

    def __init__(self, filename, query=None):
        self.uri = self.HOST_PATH + filename + "?" + query

    def get_data(self):
        rdata = requests.get(self.uri)
        jdata = rdata.json()
        return jdata

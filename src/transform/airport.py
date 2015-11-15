#!/usr/bin/python3

"""
transform.airport
~~~~~~~~~~~~~~~~~

This module implements classes for transforming extracted datasets related to
airport data.
"""

import json


class Fr24AirportTransform:

    def __init__(self, data, verbose=False):
        self.verbose = verbose
        self.data = self.get_json_data(data=data)
        # self.dep_list = self.get_depatures(data=self.data)

    def get_json_data(self, data):
        jdata_list = [
            json.loads(page.data)['result']['response']['airport']
            ['pluginData'] for page in data]
        # flatten data list
        jdata = {}
        jdata['details'] = jdata_list[0]['details']
        jdata['weather'] = jdata_list[0]['weather']
        jdata['arrivals'] = [
            arrival for page in jdata_list for
            arrival in page['schedule']['arrivals']['data']]
        jdata['departures'] = [
            arrival for page in jdata_list for
            arrival in page['schedule']['departures']['data']]
        return jdata

    def get_arrivals(self):
        """Returns a list of arriving flights"""
        return [flight['flight']['identification']['number']['default']
                for flight in self.data['arrivals']]

    def get_departures(self):
        """Returns a list of arriving flights"""
        return [flight['flight']['identification']['number']['default']
                for flight in self.data['departures']]

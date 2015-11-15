#!/usr/bin/python3

"""
transform.flight
~~~~~~~~~~~~~~~~

This module implements classes for transforming extracted datasets related to
airport data.
"""

import json


class Fr24FlightListTransform:

    def __init__(self, data, verbose=False):
        self.verbose = verbose
        raw_jdata = self.get_json_data(data=data)
        self.data = self.transform(data=raw_jdata)

    def get_json_data(self, data):
        return json.loads(data)['result']['response']['data']

    def transform(self, data):
        # trim future schedule flights
        retval = {}
        current_flights = [flight for flight in data
                           if (flight['identification']['id'] is not None) and
                           (flight['time']['real']['arrival'] is not None)]
        ap_data = data[0]['airport']
        retval['origin'] = ap_data['origin']['code']['icao']
        retval['destination'] = ap_data['destination']['code']['icao']
        retval['flight'] = [{
            'aircraft': flight['aircraft']['model']['code'],
            'reg': flight['aircraft']['registration'],
            'id': flight['identification']['id'],
            'dep_time': flight['time']['real']['departure'],
            'arr_time': flight['time']['real']['arrival']
            } for flight in current_flights]
        return retval

    def get_id_list(self):
        return [flight['id'] for flight in self.data['flight']]


class Fr24FlightDataTransform:
    # - lat
    # - lon
    # - alt
    # - gs
    # - time

    def __init__(self, data, verbose=False):
        self.verbose = verbose
        raw_jdata = self.get_json_data(data=data)
        self.data = self.transform(data=raw_jdata)

    def get_json_data(self, data):
        return json.loads(data)

    def transform(self, data):
        retval = {}
        # deflat data
        flat_data = data['trail']
        retval['trail_raw'] = [flat_data[i:i+5]
                               for i in range(0, len(flat_data), 5)]
        return retval

#!/usr/bin/python3

"""
load.geojson_out
~~~~~~~~~~~~~~~~

This module implements classes for exporting data in Geo JSON format.
"""

import json


class GeoJsonOut:

    def __init__(self, trail, verbose=False):
        self.verbose = verbose
        coordinates = self.convert_trail(trail=trail)
        self.jdata = {}
        self.jdata['type'] = 'FeatureCollection'
        self.jdata['features'] = []
        self.jdata['features'].append({})
        self.jdata['features'][0]['type'] = 'Feature'
        self.jdata['features'][0]['properties'] = {}
        self.jdata['features'][0]['geometry'] = {}
        self.jdata['features'][0]['geometry']['type'] = 'LineString'
        self.jdata['features'][0]['geometry']['coordinates'] = coordinates

    def convert_trail(self, trail):
        return [[pt[0], pt[1], pt[2]] for pt in trail]

    def export(self, filename):
        with open(str(filename), mode='w') as file_:
            self.trace('Exporting GeoJSON file {}'.format(filename))
            json.dump(self.jdata, file_)

    def trace(self, text):
        if self.verbose is True:
            print(text)


def main(verbose):
    trail = [
        [0.123, 11.2233, 42.42, 999, 9],
        [0.123, 11.2233, 42.42, 999, 9],
        [0.123, 11.2233, 42.42, 999, 9],
        [0.123, 11.2233, 42.42, 999, 9],
        [0.123, 11.2233, 42.42, 999, 9]
    ]
    json_out = GeoJsonOut(trail=trail, verbose=verbose)
    json_out.export('test.json')

if __name__ == "__main__":
    main(verbose=True)

#!/usr/bin/python3

"""
load.geojson_out
~~~~~~~~~~~~~~~~

This module implements classes for exporting data in Geo JSON format.
"""

import json


class GeoJsonOut:

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.jdata = {}
        self.jdata['type'] = 'FeatureCollection'
        self.jdata['features'] = []

    def add_2d_trail(self, metadata, trail, lat_index=0, lon_index=1):
        """Add a LineString feature derived from the given list of points
        metadata is a dict:
        - flight: flight number
        - date: flight date
        - id: flight id
        """
        # SimpleStyle spec 1.1.0 https://github.com/mapbox/simplestyle-spec
        properties = {}
        if metadata is not None:
            properties['title'] = metadata['flight']
            properties['description'] = 'id: {}; date {}'.format(
                metadata['id'], metadata['date'])
        properties['stroke'] = '#{}{}{}'.format(1, 2, 3)

        geometry = {}
        geometry['coordinates'] = [[pt[lat_index], pt[lon_index]]
                                   for pt in trail]
        geometry['type'] = 'LineString'

        feature = {}
        feature['type'] = 'Feature'
        feature['properties'] = properties
        feature['geometry'] = geometry
        self.jdata['features'].append(feature)

    def add_2d_trail_list(self, trail_list, lat_index=0, lon_index=1):
        for trail in trail_list:
            self.add_2d_trail(metadata=None, trail=trail,
                              lat_index=lat_index, lon_index=lon_index)

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
    json_out = GeoJsonOut(verbose=verbose)
    json_out.add_2d_trail(metadata=None, trail=trail)
    json_out.export('test.json')

if __name__ == "__main__":
    main(verbose=True)

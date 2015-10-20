#!/usr/bin/python3

"""
f24.zones
~~~~~~~~~

This module contains the class handling zones data
"""

from jsondl import JsonDl


class Airport:

    DEFAULT_ZONES_URL = "http://www.flightradar24.com/js/zones.js.php"

    def __init__(self, url=None):
        if url is None:
            self.url = self.DEFAULT_ZONES_URL

    def load(self):
        dl = JsonDl(self.url)
        self.zones_list = dl.getJson()

    def print_version(self):
        print(self.zones_list["version"])

    def get_zones(self):
        return self.zones_list.keys()

    def get_subzones(self, zone):
        return self.zones_list[zone]

    def print_zones(self):
        print(self.get_zones())

    def print_subzones(self, zone):
        print(self.get_subzones(zone))

    def dump_json(self):
        print(self.zones_list)


def main():
    zones = Zones()
    zones.load()
    zones.print_version()
    # zones.print_zones()
    zones.print_subzones("europe")
    # zones.dump_json()


if __name__ == "__main__":
    main()

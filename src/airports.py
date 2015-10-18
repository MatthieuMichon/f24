#!/usr/bin/python3

"""
f24.ap
~~~~~~

This module contains the class handling airports data
"""

import json
from jsondl import JsonDl


class Airports:

    DEFAULT_AP_URL = "http://www.flightradar24.com/_json/airports.php"
    # DEFAULT_AP_STATS_URL = "http://lhr.data.fr24.com/_external/dataFeedAirport.php?type=stats&continent=0&limit=5&callback=displayAirportsStats&_=1445206689193"

    def __init__(self, url=None):
        if url is None:
            self.url = self.DEFAULT_AP_URL

    def load(self):
        dl = JsonDl(self.url)
        self.ap_list = dl.getJson()

    def get_by_icao(self, icao):
        for ap in self.ap_list["rows"]:
            if ap["icao"] == icao:
                return ap
        return None

    def print_version(self):
        print(self.ap_list["version"])

    def print_by_icao(self, icao):
        print("Airport: ", icao, "; json: ", self.get_by_icao(icao))

    def dump_json(self):
        print(self.ap_list)


def main():
    ap = Airports()
    ap.load()
    ap.print_version()
    ap.print_by_icao("LFPG")
    ap.print_by_icao("RJOO")
    # ap.dump_json()


if __name__ == "__main__":
    main()

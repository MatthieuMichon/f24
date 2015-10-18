#!/usr/bin/python3

"""
f24.flight_list
~~~~~~~~~~~~~~~

This module contains the class handling playback data
"""

import time
from jsondl import JsonDl


class FlightList:

    DEFAULT_FL_URL = "http://mobile.api.fr24.com/common/v1/flight/list.json?" \
                     "fetchBy=reg&query="

    def __init__(self, url=None, reg=None):
        if url is None:
            self.url = self.DEFAULT_FL_URL + reg
        else:
            self.url = url + reg
        self.jdata = JsonDl(self.url).getJson()
        self.list = self.jdata["result"]["response"]["data"]

    def print_past_flights(self):
        for flight in self.list:
            time_departure = time.strftime(
                "%m/%d/%Y %H:%M:%S",
                time.gmtime(flight["time"]["real"]["departure"]))
            print("Airport:", flight["airport"]["origin"]["code"]["icao"],
                  "->", flight["airport"]["destination"]["code"]["icao"],
                  "date:", time_departure)


def main():
    fl = FlightList(reg="ja823a")
    fl.print_past_flights()


if __name__ == "__main__":
    main()

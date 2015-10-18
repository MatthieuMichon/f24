#!/usr/bin/python3

"""
f24.playback
~~~~~~~~~~~~

This module contains the class handling playback data
"""

from jsondl import JsonDl


class Playback:

    DEFAULT_PB_URL = "http://mobile.api.fr24.com/" \
                     "common/v1/flight-playback.json?flightId="

    def __init__(self, url=None, fid=None):
        if url is None:
            self.url = self.DEFAULT_PB_URL + fid
        else:
            self.url = url + fid
        self.jdata = JsonDl(self.url).getJson()
        self.analyze()
        self.track = self.jdata["result"]["response"]["data"]["flight"]["track"]

    def print_aircraft(self):
        print(
            "Aircraft: ", self.jdata["result"]["response"]["data"]["flight"]["aircraft"])


def main():
    pb = Playback(fid="7aca4aa")
    pb.print_aircraft()


if __name__ == "__main__":
    main()

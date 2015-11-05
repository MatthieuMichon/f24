#!/usr/bin/python3

"""
f24.playback
~~~~~~~~~~~~

This module contains the class handling playback data
"""

import matplotlib.pyplot as plt
from data_suppliers.fr24_mobile_api import Fr24MobileApi


class Playback:

    FILENAME = "flight-playback.json"

    def __init__(self, flight_id):
        self.flight_id = flight_id
        query = "flightId={}".format(self.flight_id)
        supplier = Fr24MobileApi(filename=self.FILENAME, query=query)
        self.jdata = supplier.get_data()["result"]["response"]["data"]
        self.track = self.jdata["flight"]["track"]

    def print_track_stats(self):
        print("Track data:")
        print(" - Total points: {}".format(len(self.track)))

    def get_alt(self):
        return [pt["altitude"]["feet"] for pt in self.track]

    def get_gs(self):
        return [pt["speed"]["kts"] for pt in self.track]


def main():
    pb = Playback(flight_id="7cb6b2f")
    plt.figure(1)
    plt.subplot(211)
    plt.plot(pb.get_alt())
    plt.subplot(212)
    plt.plot(pb.get_gs())
    plt.show()

if __name__ == "__main__":
    main()

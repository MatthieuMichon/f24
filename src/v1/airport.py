#!/usr/bin/python3

"""
f24.airport
~~~~~~~~~~~

This module contains the class handling airport data
"""

from data_suppliers.fr24_mobile_api import Fr24MobileApi


class Aiport:

    FILENAME = "airport.json"

    def __init__(self, code):
        self.code = code
        query = "code=" + self.code
        mapi = Fr24MobileApi(filename=self.FILENAME, query=query)
        self.jdata = mapi.get_data()

    def print_data(self):
        print("Airport: "+self.code)
        data = self.jdata["result"]["response"]["airlines"]["codeshare"]
        for key, data in data.items():
            iata = data["code"]["iata"]
            icao = data["code"]["icao"]
            name = data["name"]
            print("IATA: " + iata + "; ICAO: " + icao + "; name: " + name)
        data = self.jdata["result"]["response"]["airport"]["pluginData"]
        arrivals = data["schedule"]["arrivals"]["data"]
        for data in arrivals:
            co = data["flight"]["airline"]["name"]
            cs = data["flight"]["identification"]["callsign"]
            if cs is None:
                cs = "--"
            print("Airline: " + co + "; callsign: " + cs)


def main():
    ap = Aiport(code="RJTT")
    ap.print_data()

if __name__ == "__main__":
    main()

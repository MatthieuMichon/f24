#!/usr/bin/python3

"""
f24.al
~~~~~~

This module contains the class handling airlines data
"""

from jsondl import JsonDl


class Airlines:

    DEFAULT_AP_URL = "http://www.flightradar24.com/_json/airlines.php"

    def __init__(self, url=None):
        if url is None:
            self.url = self.DEFAULT_AP_URL

    def load(self):
        dl = JsonDl(self.url)
        self.al_list = dl.getJson()

    def get_by_code(self, code):
        for al in self.al_list["rows"]:
            if al["Code"] == code:
                return al
        return None

    def print_version(self):
        print(self.al_list["version"])

    def print_by_code(self, code):
        print("Airline: ", code, "; json: ", self.get_by_code(code))

    def dump_json(self):
        print(self.ap_list)


def main():
    al = Airlines()
    al.load()
    al.print_version()
    al.print_by_code("NH")
    # al.print_by_icao("RJOO")
    #al.dump_json()


if __name__ == "__main__":
    main()

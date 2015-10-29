#!/usr/bin/python3

"""
f24.airlines
~~~~~~~~~~~~

This module transforms airline data into a dictionnary.
"""

from data_suppliers.fr24_direct import Fr24Direct
import time


class Airlines:

    FILENAME = "_json/airlines.php"

    def __init__(self, url=None):
        self.airline_list = {}
        fr24 = Fr24Direct(filename=self.FILENAME)
        self.fr24_list = fr24.get_data()

    def map_fr24(self, fr24_list):
        for fr24_airline in fr24_list:
            if fr24_airline['Code'] not in self.airline_list:
                self.airline_list[fr24_airline['Code']] = {
                    'IATA': fr24_airline['Code'],
                    'ICAO': fr24_airline['ICAO'],
                    'Callsign': None}
            else:
                # Entry already present: check consistency
                if self.airline_list[fr24_airline['Code']]

    def print_info(self):
        print('fr24 airline list:')
        ts = self.fr24_list['version']
        ts_str = time.strftime('%Y%m%d%H%M', time.gmtime(ts))
        print('- spdated: {} / {}'.format(ts, ts_str))
        print('- airlines: {}'.format(len(self.fr24_list['rows'])))

    def get_by_code(self, code):
        airlines = self.fr24_list['rows']
        return [x for x in airlines if x['Code'] == code][0]

    def print_by_code(self, code):
        print("Airline: ", code, "; json: ", self.get_by_code(code))


def main():
    al = Airlines()
    al.print_info()
    al.print_by_code("A3")

if __name__ == "__main__":
    main()

#!/usr/bin/python3

'''
f24.flight_list
~~~~~~~~~~~~~~~

This module contains the class handling playback data
'''

import time
from data_suppliers.fr24_mobile_api import Fr24MobileApi


class FlightList:

    FILENAME = 'flight/list.json'
    QUERY = 'fetchBy=reg&query='

    def __init__(self, reg):
        self.reg = reg
        query = '{}{}'.format(self.QUERY, self.reg)
        supplier = Fr24MobileApi(filename=self.FILENAME, query=query)
        self.list = supplier.get_data()['result']['response']['data']

    def print_past_flights(self):
        for flight in self.list:
            try:
                time_departure = time.strftime(
                    '%m/%d/%Y %H:%M:%S',
                    time.gmtime(flight['time']['real']['departure']))
                orig = flight['airport']['origin']['code']['icao']
                dest = flight['airport']['destination']['code']['icao']
                callsign = flight['identification']['callsign']
                id_ = flight['identification']['id']
                if orig is not None and dest is not None:
                    print('date: {}; {} -> {}; callsign: {}; id: {}'.format(
                            time_departure, orig, dest, callsign, id_))
            except:
                continue

    def get_flight(self):
        pass


def main():
    fl = FlightList(reg='c-ghpv')
    fl.print_past_flights()


if __name__ == '__main__':
    main()

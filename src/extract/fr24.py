#!/usr/bin/python3

"""
extract.fr24
~~~~~~~~~~~~

This module implements objects extracted from fr24.com website.
"""

import time
from cache import Cache


class Fr24Airlines:
    """fr24.com airline list
    """

    URI = 'http://www.flightradar24.com/_json/airlines.php'

    def __init__(self, verbose=False):
        self.cache = Cache(verbose=verbose)
        self.update()

    def update(self):
        self.data = self.cache.lookup(uri=self.URI)


class Fr24Airports:
    """fr24.com airport list
    """

    URI = 'http://www.flightradar24.com/_json/airports.php'

    def __init__(self, verbose=False):
        self.cache = Cache(verbose=verbose)
        self.update()

    def update(self):
        self.data = self.cache.lookup(uri=self.URI)


class Fr24Airport:
    """fr24.com airport information
    interactive object: the airport must be specified
    """

    BASE_URI = 'http://mobile.api.fr24.com/common/v1/airport.json?code='

    def __init__(self, icao, verbose=False):
        """Constructor
        :param string icao: Four-char airport ICAO designator
        """
        self.cache = Cache(verbose=verbose)
        self.uri = '{}{}'.format(self.BASE_URI, icao)
        self.update()

    def update(self):
        self.data = self.cache.lookup(uri=self.uri)


def main():

    al = Fr24Airlines(verbose=True)
    print('Fr24 Airlines DB:')
    print(' - Timestamp: {} {}'.format(al.data['version'],
          time.strftime('%Y%m%d:%H%M', time.gmtime(al.data['version']))))
    print(' - Entries: {}'.format(len(al.data['rows'])))
    print(' - Row 0: {}'.format(al.data['rows'][0]))
    print(' - Row 10: {}'.format(al.data['rows'][10]))
    print(' - Row 100: {}'.format(al.data['rows'][100]))
    print(' - Row 1000: {}'.format(al.data['rows'][1000]))
    print(' - Last row: {}'.format(al.data['rows'][len(al.data['rows'])-1]))

    apl = Fr24Airports(verbose=True)
    print('Fr24 Airports DB:')
    print(' - Timestamp: {} {}'.format(apl.data['version'],
          time.strftime('%Y%m%d:%H%M', time.gmtime(apl.data['version']))))
    print(' - Entries: {}'.format(len(apl.data['rows'])))
    print(' - Row 0: {}'.format(apl.data['rows'][0]))
    print(' - Row 10: {}'.format(apl.data['rows'][10]))
    print(' - Row 100: {}'.format(apl.data['rows'][100]))
    print(' - Row 1000: {}'.format(apl.data['rows'][1000]))
    print(' - Last row: {}'.format(apl.data['rows'][len(apl.data['rows'])-1]))

    ap = Fr24Airport(icao='RJTT', verbose=True)
    ap_req = ap.data['result']['request']
    ap_ts = ap_req['plugin-setting']['schedule']['timestamp']
    print('Fr24 Airport info:')
    print(' - Timestamp: {} {}'.format(
        ap_ts, time.strftime('%Y%m%d:%H%M', time.gmtime(ap_ts))))
    print(' - Data: {}'.format(ap.data['result']))

if __name__ == "__main__":
    main()

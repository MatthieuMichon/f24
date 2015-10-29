#!/usr/bin/python3

"""
extract.fr24
~~~~~~~~~~~~

This module implements objects extracted from fr24.com website.
"""

import time
from cache import Cache


class Fr24Base:
    """fr24.com base access class
    """

    def __init__(self, uri, verbose=False):
        self.uri = uri
        self.cache = Cache(verbose=verbose)
        self.update()

    def update(self):
        self.data = self.cache.lookup(uri=self.uri)


class Fr24Airlines(Fr24Base):
    """fr24.com airline list
    """

    URI = 'http://www.flightradar24.com/_json/airlines.php'

    def __init__(self, verbose=False):
        super().__init__(uri=self.URI, verbose=verbose)


class Fr24Airports(Fr24Base):
    """fr24.com airport list
    """

    URI = 'http://www.flightradar24.com/_json/airports.php'

    def __init__(self, verbose=False):
        super().__init__(uri=self.URI, verbose=verbose)


class Fr24Planes(Fr24Base):
    """fr24.com plane list
    """

    URI = 'http://data.flightradar24.com/_external/planes.php'

    def __init__(self, verbose=False):
        super().__init__(uri=self.URI, verbose=verbose)


class Fr24Airport(Fr24Base):
    """fr24.com airport information
    interactive object: the airport must be specified
    """

    BASE_URI = 'http://mobile.api.fr24.com/common/v1/airport.json?code='

    def __init__(self, icao, verbose=False):
        """Constructor
        :param string icao: Four-char airport ICAO designator
        """
        uri = '{}{}'.format(self.BASE_URI, icao)
        super().__init__(uri=uri, verbose=verbose)


class Fr24Flight(Fr24Base):
    """fr24.com flight information
    interactive object: the flight id must be specified
    """

    BASE_URI = ('http://data.flightradar24.com/_external/'
                'planedata_json.1.4.php?format=2&f=7d4b708&')

    def __init__(self, flight_id, verbose=False):
        """Constructor
        :param string flight_id: fr24 internal seven-char hex flight id
        """
        uri = '{}{}'.format(self.BASE_URI, flight_id)
        super().__init__(uri=uri, verbose=verbose)


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

    pl = Fr24Planes(verbose=True)
    print('Fr24 Planes DB:')
    print('- Number of planes: {}'.format(len(pl.data)))

    ap = Fr24Airport(icao='RJTT', verbose=True)
    ap_req = ap.data['result']['request']
    ap_ts = ap_req['plugin-setting']['schedule']['timestamp']
    print('Fr24 Airport info:')
    print(' - Timestamp: {} {}'.format(
        ap_ts, time.strftime('%Y%m%d:%H%M', time.gmtime(ap_ts))))
    print(' - Data: {}'.format(ap.data['result']))

    fl = Fr24Flight(flight_id='7d4b708', verbose=True)
    print('Fr24 Flight info:')
    print('- Number of points: {}'.format(len(fl.data['trail'])))


if __name__ == "__main__":
    main()

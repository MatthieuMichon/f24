#!/usr/bin/python3

"""
extract.fr24
~~~~~~~~~~~~

This module implements classes for extracting datasets from fr24.com.
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
    """fr24.com airplane list
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
                'planedata_json.1.4.php?format=2&f=')

    def __init__(self, flight_id, verbose=False):
        """Constructor
        :param string flight_id: fr24 internal seven-char hex flight id
        """
        uri = '{}{}'.format(self.BASE_URI, flight_id)
        super().__init__(uri=uri, verbose=verbose)


class Fr24Plane(Fr24Base):
    """fr24.com aircraft information
    interactive object: the aircraft reg must be specified
    """

    BASE_URI = 'http://data.flightradar24.com/zones/fcgi/feed.js?reg='

    def __init__(self, reg, verbose=False):
        """Constructor
        :param string reg: exact aircraft registration (including dash)
        """
        uri = '{}{}'.format(self.BASE_URI, reg)
        super().__init__(uri=uri, verbose=verbose)


class Fr24Find(Fr24Base):
    """fr24.com find request
    interactive object: a query argument must be specified
    """

    LIMIT = 16
    BASE_URI = ('http://www.flightradar24.com/v1/search/web/find?'
                'limit={}&query='.format(LIMIT))

    def __init__(self, query, verbose=False):
        """Constructor
        :param string reg: exact aircraft registration (including dash)
        """
        uri = '{}{}'.format(self.BASE_URI, query)
        super().__init__(uri=uri, verbose=verbose)


class Fr24AutoCompAirplanes(Fr24Base):
    """fr24.com autocomplete airplanes request
    interactive object: a query argument must be specified
    """

    BASE_URI = ('http://www.flightradar24.com/data/_ajaxcalls/'
                'autocomplete_airplanes.php?&term=')

    def __init__(self, query, verbose=False):
        """Constructor
        :param string reg: exact aircraft registration (including dash)
        """
        uri = '{}{}'.format(self.BASE_URI, query)
        super().__init__(uri=uri, verbose=verbose)


# Testing

def test_Fr24Airlines(verbose):
    al = Fr24Airlines(verbose=verbose)
    print('Fr24 Airlines DB:')
    print(' - Timestamp: {} {}'.format(al.data['version'],
          time.strftime('%Y%m%d:%H%M', time.gmtime(al.data['version']))))
    print(' - Entries: {}'.format(len(al.data['rows'])))
    print(' - Row 0: {}'.format(al.data['rows'][0]))
    print(' - Row 10: {}'.format(al.data['rows'][10]))
    print(' - Row 100: {}'.format(al.data['rows'][100]))
    print(' - Row 1000: {}'.format(al.data['rows'][1000]))
    print(' - Last row: {}'.format(al.data['rows'][len(al.data['rows'])-1]))


def test_Fr24Airports(verbose):
    apl = Fr24Airports(verbose=verbose)
    print('Fr24 Airports DB:')
    print(' - Timestamp: {} {}'.format(apl.data['version'],
          time.strftime('%Y%m%d:%H%M', time.gmtime(apl.data['version']))))
    print(' - Entries: {}'.format(len(apl.data['rows'])))
    print(' - Row 0: {}'.format(apl.data['rows'][0]))
    print(' - Row 10: {}'.format(apl.data['rows'][10]))
    print(' - Row 100: {}'.format(apl.data['rows'][100]))
    print(' - Row 1000: {}'.format(apl.data['rows'][1000]))
    print(' - Last row: {}'.format(apl.data['rows'][len(apl.data['rows'])-1]))


def test_Fr24Planes(verbose):
    pl = Fr24Planes(verbose=verbose)
    print('Fr24 Planes DB:')
    print('- Number of planes: {}'.format(len(pl.data)))


def test_Fr24Airport(icao, verbose):
    ap = Fr24Airport(icao='RJTT', verbose=verbose)
    ap_req = ap.data['result']['request']
    ap_ts = ap_req['plugin-setting']['schedule']['timestamp']
    print('Fr24 Airport info:')
    print(' - Timestamp: {} {}'.format(
        ap_ts, time.strftime('%Y%m%d:%H%M', time.gmtime(ap_ts))))
    print(' - Data: {}'.format(ap.data['result']))


def test_Fr24Flight(flight_id, verbose):
    fl = Fr24Flight(flight_id=flight_id, verbose=verbose)
    print('Fr24 Flight info:')
    print(' - Number of points: {}'.format(len(fl.data['trail'])))


def test_Fr24Plane(reg, verbose):
    fp = Fr24Plane(reg=reg, verbose=verbose)
    print('Fr24 Plane info:')
    print(' - Records: {}'.format(len(fp.data)))


def test_Fr24Find(query, verbose):
    ff = Fr24Find(query=query, verbose=verbose)
    print('Fr24 Find query:')
    print(' - Number of records: {}'.format(len(ff.data['results'])))


def main():
    verbose = True
    # test_Fr24Planes(verbose=verbose)
    # test_Fr24Airports(verbose=verbose)
    # test_Fr24Planes(verbose=verbose)
    # test_Fr24Airport(icao='RJTT', verbose=verbose)
    # test_Fr24Flight(flight_id='7d4b708', verbose=verbose)
    # test_Fr24Plane(reg='JA732A', verbose=verbose)
    test_Fr24Find(query='RJTT', verbose=verbose)


if __name__ == "__main__":
    main()

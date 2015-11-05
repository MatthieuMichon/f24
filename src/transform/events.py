#!/usr/bin/python3

import re
from bs4 import BeautifulSoup


"""
    extract.avherald
    ~~~~~~~~~~~~~~~~

    This module implements classes for transforming datasets holding event
    information.
"""


class AvheraldEvent():

    REGEX_DICT = {
        'reg': r'registration ([-\w]+)',
        'flight': r'flight ([-\w]+)',
        'origin': r'from (.+?) to',
        'destination': r'to (.+?)(?:, |with)',
        'phase': r'was (.+?) when',
        'event': r'when (.+?)\.'
    }

    def __init__(self, event_data, verbose=False):
        self.verbose = verbose
        self.data = self.transform(data=event_data)

    def transform(self, data):
        text = list(data[1].stripped_strings)[1]
        data = {
            k: self.match_first(regex=self.REGEX_DICT[k], data=text)
            for k in self.REGEX_DICT.keys()}
        return data

    def match_first(self, regex, data):
        match = re.search(regex, data)
        if match:
            return match.group(1)
        else:
            return 'N/A'


class AvheraldTransfrom():
    """Transforms data obtained from avherald.com:
    - Main page
    - Events present on main page

    Creates a new Event instance with the obtained data
    """

    def __init__(self, extracted_data, verbose=False):
        self.ea = [
            AvheraldEvent(event_data=event, verbose=verbose)
            for event in extracted_data['events']]

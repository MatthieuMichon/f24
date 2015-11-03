#!/usr/bin/python3

"""
extract.avherald
~~~~~~~~~~~~~~~~

This module implements classes for extracting datasets from avherald.com.
"""

import re
import time
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
from cache import Cache


class AvheraldBase(metaclass=ABCMeta):
    """avherald.com base access class
    """

    def __init__(self, uri, verbose=False):
        self.uri = uri
        self.cache = Cache(verbose=verbose)
        self.update()

    def update(self):
        data = self.cache.lookup(uri=self.uri)
        self.soup = BeautifulSoup(data, 'lxml')
        self.trim()

    @abstractmethod
    def trim(self):
        pass


class AvheraldMain(AvheraldBase):
    """avherald.com main page
    """

    URI = 'http://avherald.com'

    def __init__(self, verbose=False):
        self.verbose = verbose
        super().__init__(uri=self.URI, verbose=verbose)

    def trim(self):
        """Remove unrelated HTML"""
        self.data = self.soup.select_one('#ad1cell')


class AvheraldArticle(AvheraldBase):
    """avherald.com article
    """

    BASE_URI = 'http://avherald.com/?article='

    def __init__(self, article, verbose=False):
        self.verbose = verbose
        uri = '{}{}'.format(self.BASE_URI, article)
        super().__init__(uri=uri, verbose=verbose)

    def trim(self):
        """Remove unrelated HTML"""
        text = self.soup.select_one('#ad1cell')
        self.data = [text.p, text.table]


def main():
    avh = AvheraldMain()
    print(avh.data)
    # links = ah.get_occurences()
    # print(links[0])

if __name__ == "__main__":
    main()

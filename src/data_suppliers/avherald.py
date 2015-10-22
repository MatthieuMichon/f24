#!/usr/bin/python3

"""
f24.data_suppliers.avherald
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class handling data supply from the Aviation Herald.
"""

import requests
from bs4 import BeautifulSoup


class Avherald:

    MAIN_URI = 'http://avherald.com/'
    HEADLINE_CLASS = '.headline_avherald'

    def __init__(self):
        main = self.fetch_main(uri=self.MAIN_URI)
        self.occurences = self.process_main(main)

    def fetch_main(self, uri):
        return requests.get(uri).text

    def process_main(self, data):
        headlines = BeautifulSoup(data).select(self.HEADLINE_CLASS)
        return [headline.parent for headline in headlines]

    def print_occurences(self):
        print(self.occurences)


def main():
    ah = Avherald()
    ah.print_occurences()

if __name__ == "__main__":
    main()

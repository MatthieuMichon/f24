#!/usr/bin/python3

import re
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
from cache import Cache

"""
extract.avherald
~~~~~~~~~~~~~~~~

This module implements classes for extracting datasets from avherald.com.
"""


class AvheraldBase():
    """avherald.com base access class
    """
    __metaclass__ = ABCMeta

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
        raise ValueError


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
        self.data = {}
        uri = '{}{}'.format(self.BASE_URI, article)
        super().__init__(uri=uri, verbose=verbose)

    def trim(self):
        """Remove unrelated HTML"""
        self.data['title'] = self.soup.title.text
        text = self.soup.select_one('#ad1cell')
        print('#### {}'.format(len(text)))
        self.data = [text.p, text.table]


class AvheraldExtract():

    ARTICLE_ID_REGEX = r'article=(\w+)&'

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.data = {}
        self.update()

    def update(self):
        avh_main = AvheraldMain(verbose=self.verbose)
        self.data['main'] = str(avh_main.data)
        id_list = re.findall(self.ARTICLE_ID_REGEX, str(avh_main.data))
        for id_ in id_list:
            aa = AvheraldArticle(article=id_, verbose=self.verbose)
            #print(aa.data)


def main():
    ae = AvheraldExtract(verbose=True)
    #print(ae.get_articles())
    # links = ah.get_occurences()
    # print(links[0])

if __name__ == "__main__":
    main()

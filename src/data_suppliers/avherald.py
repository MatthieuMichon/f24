#!/usr/bin/python3

"""
f24.data_suppliers.avherald
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class handling data supply from the Aviation Herald.
"""

import re
import requests
from bs4 import BeautifulSoup
from cache import Cache


class Avherald:

    MAIN_URI = 'http://avherald.com/'
    HEADLINE_CLASS = '.headline_avherald'
    ARTICLE_ID = '#ad1cell'
    HEADLINE_SELECTOR = '.headline_article'
    TIME_SELECTOR = '.time_avherald'
    TEXT_CLASS = 'sitetext'

    def __init__(self):
        top = self.fetch_uri(uri=self.MAIN_URI)
        self.occurences = self.process_main(data=top)
        self.get_article_data(self.occurences[0])

    def fetch_uri(self, uri):
        return requests.get(uri).text

    def process_main(self, data):
        headlines = BeautifulSoup(data, 'lxml').select(self.HEADLINE_CLASS)
        headlines_links = [headline.parent for headline in headlines]
        links = [link.get('href') for link in headlines_links]
        return links

    def get_occurences(self):
        return self.occurences

    def get_article_data(self, article_id):
        uri = self.MAIN_URI + article_id
        cache = Cache()
        cache_lookup = cache.lookup(uri=uri)
        if cache_lookup is not None:
            print('Cache hit')
            html = cache_lookup
        else:
            print('Cache miss')
            html = self.fetch_uri(uri=uri)
            cache.store(uri=uri, data=html)
        bs = BeautifulSoup(html, 'lxml').select(self.ARTICLE_ID)[0]
        article = {}
        article['id'] = self.re_extract(
                text=article_id, regex=r'article=([0-9a-f]+)')
        article['time'] = bs.select(self.TIME_SELECTOR)[0].string
        paragraph = bs.find_all('span', class_=self.TEXT_CLASS)
        article['headline'] = bs.select(self.HEADLINE_SELECTOR)[0].string
        match = re.search(r'registration ([-\w]+)', str(paragraph))
        # if match:
        #     article['reg'] = match.group(1)
        if self.re_extract(
                text=str(paragraph), regex=r'registration ([-\w]+)'):
            article['reg'] = match.group(1)
        print(article)

    def re_extract(self, text, regex):
        match = re.search(regex, text)
        if not match:
            return None
        return match.group(1)


def main():
    Avherald()
    # links = ah.get_occurences()
    # print(links[0])

if __name__ == "__main__":
    main()

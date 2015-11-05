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

    REG_REGEX = r'registration ([-\w]+)'

    def __init__(self, event_data, verbose=False):
        self.data = {}
        self.verbose = verbose
        self.transform(data=event_data)

    def transform(self, data):
        text = list(data[1].stripped_strings)[1]
        # print('###:'.format(text))
        self.data['reg'] = self.get_reg(data=text)

    def get_reg(self, data):
        match = re.search(self.REG_REGEX, data)
        if match:
            print(match.group(1))
            return match.group(1)
        else:
            print('N/A')
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


# [<p align="left"><span class="headline_article">Incident: Avianca A319 near Cartagena on Nov 2nd 2015, engine shut down in flight</span><br/></p>,

# <table><tr><td><span class="time_avherald">By Simon Hradecky, created Wednesday, Nov  4th 2015 22:01Z, last updated Wednesday, Nov  4th 2015 22:01Z</span>
# <p align="left"><span class="sitetext">An Avianca Airbus A319-100, registration HK-4553 performing flight AV-255 from Havana (Cuba) to Bogota (Colombia), was enroute at FL370 over the Caribbean Sea about 200nm north of Cartagena (Colombia) when the right hand engine (CFM56) began to increasingly vibrate and became increasingly noisy. The crew subsequently shut the engine down and diverted to Cartagena for a safe landing.<br/><br/>A passenger reported the vibrations became so severe that glasses were jumping on the trays and falling around. Loud scraping noises came from the right hand engine, the engine was finally shut down.<br/><br/>The aircraft is still on the ground in Cartagena about 48 hours later.<br/><br/><br/></span></p></td></tr></table>]




# class AvheraldMain:

#     MAIN_URI = 'http://avherald.com/'
#     HEADLINE_CLASS = '.headline_avherald'
#     ARTICLE_ID = '#ad1cell'
#     HEADLINE_SELECTOR = '.headline_article'
#     TEXT_CLASS = 'sitetext'

#     def __init__(self):
#         top = self.fetch_uri(uri=self.MAIN_URI)
#         self.occurences = self.process_main(data=top)

#     def get_latest(self):
#         fp = self.fetch_uri(uri=self.MAIN_URI)
#         self.occurences = self.process_main(data=fp)
#         return self.get_article_data(self.occurences[0])

#     def fetch_uri(self, uri):
#         return requests.get(uri).text

#     def process_main(self, data):
#         headlines = BeautifulSoup(data, 'lxml').select(self.HEADLINE_CLASS)
#         headlines_links = [headline.parent for headline in headlines]
#         links = [link.get('href') for link in headlines_links]
#         return links

#     def get_occurences(self):
#         return self.occurences

#     def get_article_data(self, article_id):
#         """get_article_data: returned data from given article id
#         :returns a dict:
#            - id: internal avherald ID
#            - time: time string
#            - headline: short description of the event
#            - reg: aircraft registration
#         """
#         uri = self.MAIN_URI + article_id
#         cache = Cache()
#         cache_lookup = cache.lookup(uri=uri)
#         if cache_lookup is not None:
#             print('Cache hit')
#             html = cache_lookup
#         else:
#             print('Cache miss')
#             html = self.fetch_uri(uri=uri)
#             cache.store(uri=uri, data=html)
#         bs = BeautifulSoup(html, 'lxml').select(self.ARTICLE_ID)[0]

#         article = {}
#         article['id'] = self.re_extract(
#                 text=article_id, regex=r'article=([0-9a-f]+)')
#         article['time'] = self.get_time(
#             bs.select(self.HEADLINE_SELECTOR)[0].string)
#         paragraph = bs.find_all('span', class_=self.TEXT_CLASS)
#         article['headline'] = bs.select(self.HEADLINE_SELECTOR)[0].string
#         article['reg'] = self.re_extract(
#             text=str(paragraph), regex=r'registration ([-\w]+)')
#         article['flight'] = self.re_extract(
#             text=str(paragraph), regex=r'flight ([0-9A-Z-]+)')

#         return article

#     def re_extract(self, text, regex):
#         match = re.search(regex, text)
#         if not match:
#             return None
#         return match.group(1)

#     def get_time(self, text):
#         """Extract a date string from a paragraph.
#         Return the epoch value (number of seconds since epoch)
#         """
#         date_str = self.re_extract(text=text, regex=r'on ([ \w]+),')
#         date_str = re.sub(r'(?:st|nd|rd|th)', '', date_str)
#         date = int(time.mktime(time.strptime(date_str, '%b %d %Y')))
#         return date

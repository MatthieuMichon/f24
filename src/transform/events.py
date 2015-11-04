#!/usr/bin/python3

"""
    extract.avherald
    ~~~~~~~~~~~~~~~~

    This module implements classes for transforming datasets holding event
    information.
"""


class TransfromAvh():
    """Transforms data obtained from avherald.com:
    - Main page
    - Events present on main page

    Creates a new Event instance with the obtained data
    """






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

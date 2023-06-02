from datetime import datetime

from typing import DefaultDict
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

from wikipage import WikiPage


class ScrapContributors:
    ANONUSER = 'mw-anonuserlink'

    def __init__(self, title: str, revisions: int) -> None:
        self.title = title
        self.revisions = revisions
        self.url = f'https://en.wikipedia.org/w/index.php?title={self.title}&action=history&offset=&limit={self.revisions}'
        self.loaded_data = None


    def request_data(self):
        r = requests.get(self.url)
        return r.content.decode('utf-8')


    def get_authors(self) -> DefaultDict:
        self.loaded_data = self.request_data()
        soup = BeautifulSoup(self.loaded_data, 'html.parser')

        contrib_list = soup.find_all('a', 'mw-userlink')

        dict_authors = defaultdict(int)
        for contrib in contrib_list:
            if not self.ANONUSER in contrib['class']:
                dict_authors[contrib.bdi.text] += 1
            else:
                dict_authors['anon'] += 1

        return dict_authors


    def get_dates(self) -> DefaultDict:
        if self.loaded_data is None:
            self.loaded_data = self.request_data()

        soup = BeautifulSoup(self.loaded_data, 'html.parser')

        dates_list = soup.find_all('a', 'mw-changeslist-date')
        dict_dates = defaultdict(int)
        for date in dates_list:
            dateobj = datetime.strptime(date.text, '%H:%M, %d %B %Y')
            dict_dates[dateobj.month] += 1

        return dict_dates


    def get_wikipage(self) -> WikiPage:
        return WikiPage(self.title, 
                        self.get_authors(),
                        self.get_dates())



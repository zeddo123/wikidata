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


    def request_data(self):
        r = requests.get(self.url)
        return r.content.decode('utf-8')


    def get_authors(self) -> DefaultDict:
        data = self.request_data()
        soup = BeautifulSoup(data, 'html.parser')

        contrib_list = soup.find_all('a', 'mw-userlink')

        dict_authors = defaultdict(int)
        for contrib in contrib_list:
            if not self.ANONUSER in contrib['class']:
                dict_authors[contrib.bdi.text] += 1
            else:
                dict_authors['anon'] += 1

        return dict_authors


    def get_wikipage(self) -> WikiPage:
        return WikiPage(title=self.title, authors=self.get_authors())

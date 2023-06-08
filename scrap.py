from typing import DefaultDict
from collections import defaultdict
from bs4 import BeautifulSoup
from tqdm import tqdm
import dateparser

from wikipage import WikiPage


class ScrapWiki:
    """
    ScrapWiki takes care of scraping the wikipage for contributor
    and contributions.

    Attributes:
        title: WikiPage title in url (usually in this format Xx_Yy).

        loaded_data: response from wikipedia
        soup: BeautifulSoup object

    """
    ANONUSER = 'mw-anonuserlink'

    def __init__(self, title: str, language: str, content: str) -> None:
        self.title = title
        self.language = language
        self.loaded_data = content
        self.soup = None



    def get_authors(self) -> DefaultDict:
        """
        Scraps webpage for contributors.

        Returns:
            dict_authors: dict that holds (contributor, number_of_contributions)
        """

        if self.soup is None:
            self.soup = BeautifulSoup(self.loaded_data, 'html.parser')

        contrib_list = self.soup.find_all('a', 'mw-userlink')

        dict_authors = defaultdict(int)
        for contrib in tqdm(contrib_list):
            if not self.ANONUSER in contrib['class']:
                dict_authors[contrib.bdi.text] += 1
            else:
                dict_authors['anon'] += 1

        return dict_authors


    def get_dates(self) -> DefaultDict:
        """
        Scraps webpage for the date of contributions by month.

        Returns:
            dict_dates: dict that holds (number_of_month, number_of_contributions) 

        """
        if self.soup is None:
            self.soup = BeautifulSoup(self.loaded_data, 'html.parser')

        dates_list = self.soup.find_all('a', 'mw-changeslist-date')
        dict_dates = defaultdict(int)
        for date in tqdm(dates_list):
            try:
                dateobj = dateparser.parse(date.text, languages=[self.language])
                dict_dates[dateobj.month] += 1
            except:
                print(f'Cannot parse date format {date.text} in wikipage')

        return dict_dates


    def get_wikipage(self) -> WikiPage:
        """Returns a WikiPage object for querying the data"""
        return WikiPage(self.title,
                        f'{self.title}({self.language})', 
                        self.get_authors(),
                        self.get_dates())



from collections import defaultdict
import requests
from bs4 import BeautifulSoup

from scrap import ScrapContributors


page = ScrapContributors('Errico_Malatesta', 5000).get_wikipage()
page2 = ScrapContributors('Mikhail_Bakunin', 5000).get_wikipage()
print(page.anon_contribs)
print(page.biggest_contributor)
print(page.biggest_nonanon_contributor)
print(page2.anon_contribs)
print(page2.biggest_contributor)
print(page2.biggest_nonanon_contributor)

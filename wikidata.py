from collections import defaultdict
import requests
from bs4 import BeautifulSoup

ANONUSER = 'mw-anonuserlink'
r = requests.get('https://en.wikipedia.org/w/index.php?title=Errico_Malatesta&action=history&offset=&limit=500')

content = r.content.decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')

contrib_list = soup.find_all('a', 'mw-userlink')

dict_authors = defaultdict(int)
for contrib in contrib_list:
    print(contrib.bdi.text)
    if not ANONUSER in contrib['class']:
        dict_authors[contrib.bdi.text] += 1
    else:
        dict_authors['anon'] += 1

print(dict_authors)

import argparse
import asyncio
from exceptions import PageNotFoundException

from scrap import ScrapWiki
import plot
import async_requests

import matplotlib.pyplot as plt


parser = argparse.ArgumentParser('Wikidata', description='Extracts and compares data about wikipedia pages')
parser.add_argument('page1', type=str, help='Name of Wikipedia page')
parser.add_argument('page2', type=str, help='Name of Wikipedia page')

parser.add_argument('-c', '--contributions',
                    help='Number of contributions to retrieve',
                    type=int, default=5000)
parser.add_argument('-o', '--output', type=str, default='output',
                    help='Name of output file for the graphs')
parser.add_argument('--graphical', default=True, action=argparse.BooleanOptionalAction,
                    help='Display data graphicly')
parser.add_argument('--csv-data', default=False, action=argparse.BooleanOptionalAction,
                    help='Compile contributors information per page in a csv file')
arg = parser.parse_args()


url1 = ScrapWiki(arg.page1, arg.contributions)
url2 = ScrapWiki(arg.page2, arg.contributions)

try:
    result = asyncio.run(async_requests.get([(url1.title, url1.url),
                                    (url2.title, url2.url)]))
    url1.loaded_data = result[0]
    url2.loaded_data = result[1]
except PageNotFoundException as e:
    print(f'{e}: Make sure that the Title for the page is correct.')
    exit(1)

page1 = url1.get_wikipage()
page2 = url2.get_wikipage()

plt.style.use('ggplot')
fig = plt.figure()

plot.plot_plots(page1, page2)

fig.savefig(f'{arg.output}.png', bbox_inches='tight', dpi=150)

if arg.csv_data:
    page1.contributions_to_csv()
    page2.contributions_to_csv()

if arg.graphical:
    plt.show()



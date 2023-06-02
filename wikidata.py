import argparse
import asyncio

from scrap import ScrapContributors
import plot
import async_requests

import matplotlib.pyplot as plt


parser = argparse.ArgumentParser('Wikidata', description='Extracts and compares data about wikipedia pages')
parser.add_argument('page1', type=str, help='Name of Wikipedia page')
parser.add_argument('page2', type=str, help='Name of Wikipedia page')

parser.add_argument('-c', '--contributions',
                    help='Number of contributions to retrieve',
                    type=int, default=5000)
parser.add_argument('-o', '--ouput', type=str, default='ouput',
                    help='Name of output file for the graphs')
parser.add_argument('--graphical', default=True, action=argparse.BooleanOptionalAction,
                    help='Display data graphicly')
parser.add_argument('--csv-data', default=False, action=argparse.BooleanOptionalAction,
                    help='Compile contributors information per page in a csv file')
arg = parser.parse_args()


page = ScrapContributors(arg.page1, arg.contributions)
page2 = ScrapContributors(arg.page2, arg.contributions)

result = asyncio.run(async_requests.get([(page.title, page.url),
                                (page2.title, page2.url)]))
page.loaded_data = result[0]
page2.loaded_data = result[1]

page = page.get_wikipage()
page2 = page2.get_wikipage()

plt.style.use('ggplot')

plot.plot_contributions_by_type((2, 2, 3), page, page2)
plt.tight_layout()

plot.plot_contributions_by_month((2, 2, 1), page)
plt.tight_layout()

plot.plot_contributions_by_month((2, 2, 2), page2)
plt.tight_layout()


plot.plot_venn((2, 2, 4), page, page2)
plt.tight_layout()

if arg.graphical:
    plt.show()

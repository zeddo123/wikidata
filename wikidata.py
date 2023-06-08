import argparse
import asyncio
from exceptions import PageNotFoundException
from meta_wikipage import MetaWikiPage

from scrap import ScrapWiki
import plot
import async_requests

import matplotlib.pyplot as plt


# Argparser configuration
parser = argparse.ArgumentParser('Wikidata', description='Extracts and compares data about wikipedia pages')
parser.add_argument('page1', type=str, help='Name of Wikipedia page')
parser.add_argument('page2', type=str, help='Name of Wikipedia page')

parser.add_argument('-c', '--contributions',
                    help='Number of contributions to retrieve',
                    type=int, default=5000)
parser.add_argument('-l','--languages', nargs='+', default=['en'],
                    help='Set of language')
parser.add_argument('-o', '--output', type=str, default='output',
                    help='Name of output file for the graphs')
parser.add_argument('--graphical', default=True, action=argparse.BooleanOptionalAction,
                    help='Display data graphicly')
parser.add_argument('--csv-data', default=False, action=argparse.BooleanOptionalAction,
                    help='Compile contributors information per page in a csv file')
arg = parser.parse_args()


# Create objects that take care of scrapping 
# the wikipages.
metapage1 = MetaWikiPage(arg.page1, arg.contributions, arg.languages)
metapage2 = MetaWikiPage(arg.page2, arg.contributions, arg.languages)

metapage1_content, metapage2_content = async_requests.aggregate_downloads(metapage1, metapage2)

metapage1.set_content(metapage1_content)
metapage2.set_content(metapage2_content)

pages1, pages2 = metapage1.get_pages(), metapage2.get_pages()

plt.style.use('ggplot')
fig = plt.figure(figsize=(10, 10))
#fig.subplots_adjust(top=1, bottom=0.15, left=0.2, hspace=0.8)

plot.plot_plots(pages1, pages2)

fig.savefig(f'{arg.output}.png', bbox_inches='tight', dpi=150)

# Generates csv output files (if option was selected)
if arg.csv_data:
    metapage1.contributions_to_csv()
    metapage2.contributions_to_csv()

# show plt figure (if option was selected)
if arg.graphical:
    plt.show()



from itertools import chain

import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np

from wikipage import WikiPage

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def plot_plots(pages1: list[WikiPage], pages2: list[WikiPage]):
    """
    General function to plot all graphs of pages1, and pages2.

    Args:
        pages1: list[WikiPage] List of all page1 with different languages
        pages2: list[WikiPage] List of all page2 with different languages
    """

    # Users/Anonymous contributions plot
    plot_contributions_by_type((2, 2, 2), pages1, pages2)
    plt.tight_layout()

    # Contributions per month for all languages of page1
    multiple_plot_contributions_by_month((2, 2, 1), pages1)
    plt.tight_layout()

    # Contributions per month for page 2
    multiple_plot_contributions_by_month((2, 2, 3), pages2)
    plt.tight_layout()

    plot_venn((2, 2, 4), pages1, pages2)
    plt.tight_layout()


def plot_venn(axis, pages1: list[WikiPage], pages2: list[WikiPage]):
    """
    plots the venn diagram of page1, and page2.

    Args:
        axis: axis of the matplotlib figure.
        pages1: list[WikiPage]
        pages2: list[WikiPage]
    """
    title = 'Intersection of contributors'

    all_page1_contributions = list(page1.contributors_list for page1 in pages1)
    set1 = set(chain(*all_page1_contributions))

    all_page2_contributions = list(page2.contributors_list for page2 in pages2)
    set2 = set(chain(*all_page2_contributions))

    plt.subplot(*axis)
    plt.title(title)
    venn2([set1, set2], (pages1[0].pure_title, pages2[0].pure_title))


def plot_contributions_by_type(axis, pages1: list[WikiPage], pages2: list[WikiPage]):
    """
    plots Anonymous/non-anonymous contributions of page1 and page2.

    Args:
        axis: axis of the matplotlib figure.
        pages1: list[WikiPage]
        pages2: list[WikiPage]
    """
    plt.subplot(*axis, label='Type')

    groups = [page.title for page in chain(pages1, pages2)]

    user_contribs = [page.total_user_contribs for page in chain(pages1, pages2)]
    anon_contribs = [page.anon_contribs for page in chain(pages1, pages2)]

    x_axis = np.arange(len(groups))

    plt.bar(x_axis + 0.20, user_contribs, width=0.2, label='User contribitions')
    plt.bar(x_axis + 0.20*2, anon_contribs, width=0.2, label='Anonymous contribitions')
    plt.xticks(x_axis, groups, rotation='vertical')
    plt.title('Contributions by type')
    plt.legend()


def plot_contributions_by_month(axis, page: WikiPage):
    """
    plots contributions of a WikiPage by months.

    Args:
        axis: axis of the matplotlib figure.
        page: WikiPage
    """
    plt.subplot(*axis)
    plt.title(f'{page.title}\n contributions by month')
    x, y = page.ordered_months()
    plt.bar(x, y)
    plt.xticks(x, rotation='vertical')


def multiple_plot_contributions_by_month(axis, pages: list[WikiPage]):
    """
    Plots contributions of multiple wikipages by months.

    Args:
        axis: axis of the matplotlib figure.
        pages: list[WikiPage]
    """
    plt.subplot(*axis)

    groups = MONTHS
    months_contributions = [page.ordered_months()[1] for page in pages]

    x_axis = np.arange(len(groups))

    for i, months in enumerate(months_contributions):
        plt.bar(x_axis + 0.20 * (i + 1), months, width=0.2, label=f'{pages[i].title}')

    plt.xticks(x_axis, groups, rotation='vertical')
    plt.title(f'{pages[0].pure_title}\'s monthy contribs')
    plt.legend()


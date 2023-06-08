import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np

from wikipage import WikiPage


def plot_plots(page1: WikiPage, page2: WikiPage):
    """
    General function to plot all graphs of page1, and page2.

    Args:
        page1: WikiPage
        page2: WikiPage
    """

    # Users/Anonymous contributions plot
    plot_contributions_by_type((2, 2, 3), page1, page2)
    plt.tight_layout()

    # Contributions per month for page 1
    plot_contributions_by_month((2, 2, 1), page1)
    plt.tight_layout()

    # Contributions per month for page 2
    plot_contributions_by_month((2, 2, 2), page2)
    plt.tight_layout()

    plot_venn((2, 2, 4), page1, page2)
    plt.tight_layout()


def plot_venn(axis, page1: WikiPage, page2: WikiPage):
    """
    plots the venn diagram of page1, and page2.

    Args:
        axis: axis of the matplotlib figure.
        page1: WikiPage
        page2: WikiPage
    """
    title = 'Intersection of contributors'

    set1 = set(page1.contributors_list)
    set2 = set(page2.contributors_list)

    plt.subplot(*axis)
    plt.title(title)
    venn2([set1, set2], (page1.title, page2.title))


def plot_contributions_by_type(axis, page1: WikiPage, page2: WikiPage):
    """
    plots Anonymous/non-anonymous contributions of page1 and page2.

    Args:
        axis: axis of the matplotlib figure.
        page1: WikiPage
        page2: WikiPage
    """
    plt.subplot(*axis)

    groups = [page1.title, page2.title]
    user_contribs = [page1.total_user_contribs, page2.total_user_contribs]
    anon_contribs = [page1.anon_contribs, page2.anon_contribs]

    x_axis = np.arange(len(groups))

    plt.bar(x_axis + 0.20, user_contribs, width=0.2, label='User contribitions')
    plt.bar(x_axis + 0.20*2, anon_contribs, width=0.2, label='Anonymous contribitions')
    plt.xticks(x_axis, groups)
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



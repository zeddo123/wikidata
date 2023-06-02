import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np

def plot_venn(axis, page1, page2):
    title = 'Intersection of contributors'

    set1 = set(page1.contributors_list)
    set2 = set(page2.contributors_list)

    plt.subplot(*axis)
    plt.title(title)
    venn2([set1, set2], (page1.title, page2.title))


def plot_contributions_by_type(axis, page1, page2):
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


def plot_contributions_by_month(axis, page):
    plt.subplot(*axis)
    plt.title(f'{page.title}\n contributions by month')
    x, y = page.ordered_months()
    plt.bar(x, y)
    plt.xticks(x, rotation='vertical')



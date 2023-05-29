from scrap import ScrapContributors


page = ScrapContributors('Errico_Malatesta', 5000).get_wikipage()
page2 = ScrapContributors('Mikhail_Bakunin', 5000).get_wikipage()

print(page2.get_same_contributors_as(page))

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

set1 = set(page.contributors_list)
set2 = set(page2.contributors_list)

venn2([set1, set2], (page.title, page2.title))

plt.show()

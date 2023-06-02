import asyncio

from numpy import result_type

from scrap import ScrapContributors
import plot
import async_requests

import matplotlib.pyplot as plt

page = ScrapContributors('Errico_Malatesta', 5000)
page2 = ScrapContributors('Mikhail_Bakunin', 5000)

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

plt.show()

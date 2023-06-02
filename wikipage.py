from dataclasses import dataclass
from typing import DefaultDict

@dataclass
class WikiPage:
    title: str
    authors: DefaultDict
    months: DefaultDict

    @property
    def anon_contribs(self):
        return self.authors['anon']

    
    @property
    def total_contribs(self):
        return sum(v for _, v in self.authors.items())


    @property
    def biggest_contributor(self):
        return max(self.authors, key=lambda x: self.authors[x])


    @property
    def biggest_nonanon_contributor(self):
        return max(self.authors, key=lambda x: self.authors[x] if x != 'anon' else 0)


    @property
    def contributors_list(self):
        return list(self.authors.keys())


    @property
    def total_user_contribs(self):
        return self.total_contribs - self.anon_contribs


    def get_same_contributors_as(self, other):
        contributors = []
        for key in self.authors.keys():
            if other.authors.get(key):
                contributors.append(key)
        return contributors

    
    def data_for_bar(self):
        return (list(self.authors.keys()), list(self.authors.values()))


    def ordered_months(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        contribs = []
        for i in range(1, 13):
            contribs.append(self.months[i])
        return months, contribs




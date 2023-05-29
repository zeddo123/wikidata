from dataclasses import dataclass
from typing import DefaultDict

@dataclass
class WikiPage:
    title: str
    authors: DefaultDict

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


    def get_same_contributors_as(self, other):
        contributors = []
        for key in self.authors.keys():
            if other.authors.get(key):
                contributors.append(key)
        return contributors


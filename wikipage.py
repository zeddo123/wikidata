from dataclasses import dataclass
from typing import DefaultDict

from tqdm import tqdm

@dataclass
class WikiPage:
    title: str
    authors: DefaultDict
    months: DefaultDict

    @property
    def anon_contribs(self) -> int:
        """
        Returns:
            int: Number of contributions made by anonymous contributors.
        """
        return self.authors['anon']

    
    @property
    def total_contribs(self) -> int:
        """
        Returns:
            int: Total number of contrib            
        """
        return sum(v for _, v in self.authors.items())


    @property
    def biggest_contributor(self) -> str:
        """
        Searches for the contributor with the highest number of contributions.

        Returns:
            str: biggest contributor.
        """
        return max(self.authors, key=lambda x: self.authors[x])


    @property
    def biggest_nonanon_contributor(self) -> str:
        """
        Search for the biggest contributor that is not anonymous.

        Returns:
            str: biggest contributor. 
        """
        return max(self.authors, key=lambda x: self.authors[x] if x != 'anon' else 0)


    @property
    def contributors_list(self) -> list[str]:
        """
        return the list of contributors.

        Returns:
            list[str]: list containing contributor names. 
        """
        return list(self.authors.keys())


    @property
    def total_user_contribs(self) -> int:
        """
        Calculates the number of contributions made by non-anonymous users.

        Returns:
            int: Number of contributions.

        """
        return self.total_contribs - self.anon_contribs


    def get_same_contributors_as(self, other) -> list[str]:
        """
        Finds the intersection of contributor from two wikipages.

        Args:
            other: WikiPage object.

        Returns:
            list[str]: list of common contributors.
        """
        return list(set(self.authors.keys()).intersection(set(other.authors.key())))

    
    def data_for_bar(self) -> tuple[list, list]:
        """
        Formats the data for specific way to use it in a matplotlib bar plot.

        Returns:
            tuple[list, list]: tuple of lists that contains the contributors and their contributions separately.
        """
        return (list(self.authors.keys()), list(self.authors.values()))


    def ordered_months(self) -> tuple[list, list]:
        """
        Formats the months data properly for a matplotlib bar plot.

        Returns:
            tuple[list, list]: tuple of list of months and number of contributions of those months. 
        """
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        contribs = []
        for i in range(1, 13):
            contribs.append(self.months[i])
        return months, contribs

    
    def contributions_to_csv(self):
        """Compiles the contributions data to a csv file."""
        with open(f'{self.title}_contributions.csv', 'w') as fs:
            fs.write('contributor,contributions\n')
            for key, value in tqdm(self.authors.items()):
                fs.write(f'{key},{value}\n')

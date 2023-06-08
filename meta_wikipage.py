from scrap import ScrapWiki
from wikipage import WikiPage


class MetaWikiPage:
    """
    Handels multiple languages for the same wikipedia page.

    Attributes:
        title: Title of the wikipage page usually (Xxx_Yyy)
        languages: Set of languages to be used for the meta-page.
        revisions: Number of revisions/contributions to be used.
        scraps: set of individual pages.
    """
    
    def __init__(self, title: str, revisions: int, languages: list[str]):
        self.title = title
        self.languages = languages
        self.revisions = revisions
        self.scraps = {}
        self.pages = None


    def constructUrl(self, language: str):
        return f'https://{language}.wikipedia.org/w/index.php?title={self.title}&action=history&offset=&limit={self.revisions}'


    def urls(self):
        """
        Generates all urls of the meta-page.

        Yields:
            tuple(title, language, url): url of the page with language set.
        """
        for language in self.languages:
            yield self.title, language, self.constructUrl(language)


    def set_content(self, content: dict[str, str]):
        """
        Sets the content of the pages to be 

        Args:
            content: dict with language as key, and content as value.
        """
        for language, value in content.items():
            self.scraps[language] = ScrapWiki(self.title, language, value)

    
    def get_pages(self) -> list[WikiPage]:
        self.pages = { key: value.get_wikipage() for key, value in self.scraps.items()}
        return list(self.pages.values())


    def contributions_to_csv(self):
        with open(f'{self.title}_contribs.csv', 'w') as fs:
            fs.write('contributor,contributions,language\n')
            for language, page in self.pages.items():
                for author, contribs in page.contributions():
                    fs.write(f'{author},{contribs},{language}\n')
            




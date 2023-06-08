import asyncio
from collections import defaultdict
from itertools import chain
import aiohttp
from exceptions import PageNotFoundException
from meta_wikipage import MetaWikiPage


def aggregate_downloads(meta_page1: MetaWikiPage,
                        meta_page2: MetaWikiPage):
    """
    Fetches all the pages of the metapage1 and metapage2.

    Args:
        meta_page1: meta_page1 to be used.
        meta_page2: meta_page2 to be used.

    Returns:
        tuple[dict[str, str], dict[str,str]]: first dictionary is for
        metapage1 and second metapage2's dictionary.

    """
    all_urls = list(chain(meta_page1.urls(), meta_page2.urls()))

    try:
        # Perform pages request asynchronously
        dic = asyncio.run(get(all_urls))
    except PageNotFoundException as e:
        print(f'{e}: Make sure that the Title for the page is correct.')
        exit(1)

    return dic[meta_page1.title], dic[meta_page2.title]
    

async def pull(page: tuple[str, str, str], session: aiohttp.ClientSession) -> tuple[str, str, str]:
    """
    Pull the content of page at url passed.

    Args:
        page: tuple(title, language, url)
        session: aoihttp session to make requests
    Returns:
        tuple(str, str, str): Title, language, and body of response

    Raises:
        PageNotFoundException: raised when page is not found.
    """
    title = page[0]
    language = page[1]
    url = page[2]
    try:
        async with session.get(url=url) as resp:
            if resp.status == 404:
                raise Exception()

            result = await resp.text()
            
            print(f'Finished downloading {title} {language}')
            return title, language, result
    except Exception:
        raise PageNotFoundException(f'Could not find page {title} {language}')


async def get(pages) -> dict[str, dict[str, str]]:
    """
    Returns all the content of the wikipages passed to it.

    Args:
        pages: list[tuple[str, str, str]] that contain the title, language and url of the page.

    Returns:
        dict[str, dict[str, str]]: dict containing the contents of each page.
    """
    async with aiohttp.ClientSession() as s:
        results = await asyncio.gather(*[pull(page, s) for page in pages])

    dict_content = defaultdict(dict)
    for title, language, content in results:
        dict_content[title][language] = content

    return dict_content


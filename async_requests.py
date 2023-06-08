import asyncio
import aiohttp
from exceptions import PageNotFoundException


async def pull(title, url, session: aiohttp.ClientSession):
    """
    Pull the content of page at url passed.

    Args:
        title: title of wikipage
        url: Full url of wikipage
        session: aoihttp session to make requests
    Returns:
        str: body of response

    Raises:
        PageNotFoundException: raised when page is not found.
    """
    try:
        async with session.get(url=url) as resp:
            if resp.status == 404:
                raise Exception()

            result = await resp.text()
            
            print(f'Finished downloading {title}')
            return result
    except Exception:
        raise PageNotFoundException(f'Could not find page {title}')


async def get(pages):
    """
    Returns all the content of the wikipages passed to it.

    Args:
        pages: list[tuple[str, str]] that contain the title and url of the page.

    Returns:
        list[str]: list containing the contents of each page (in the order they came in)
    """
    async with aiohttp.ClientSession() as s:
        ret = await asyncio.gather(*[pull(page[0], page[1], s) for page in pages])
    return ret


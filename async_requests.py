import asyncio
import aiohttp
from exceptions import PageNotFoundException


async def pull(title, url, session: aiohttp.ClientSession):
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
    async with aiohttp.ClientSession() as s:
        ret = await asyncio.gather(*[pull(page[0], page[1], s) for page in pages])
    return ret


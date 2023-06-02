import asyncio
import aiohttp


async def pull(title, url, session):
    try:
        async with session.get(url=url) as resp:
            result = await resp.text()
            
            print(f'Finished downloading {title}')
            return result
    except:
        print(f'Could not download {title}')


async def get(pages):
    async with aiohttp.ClientSession() as s:
        ret = await asyncio.gather(*[pull(page[0], page[1], s) for page in pages])
    return ret


import asyncio
import aiohttp


async def fetch_page(session: aiohttp.ClientSession, url: str):
    with aiohttp.Timeout(10):
        async with session.get(url) as resp:
            assert resp.status == 200
            return await resp.read()


loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
    content = loop.run_until_complete(fetch_page(session, 'http://qq.com'))
    print(content)

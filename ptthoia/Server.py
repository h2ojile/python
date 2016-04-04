from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello {}'.format(name)
    return web.Response(text=text)


app = web.Application()
app.router.add_route('GET', '/{name}', handle)
web.run_app(app, port = 80)

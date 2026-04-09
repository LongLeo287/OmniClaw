import asyncio
from aiohttp import web

class FireCrawlMCP:
    def __init__(self):
        self.app = web.Application()
        self.routes = web.RouteTableDef()

    async def start(self):
        for route in self.routes:
            self.app.router.add_route(route.method, route.path, route.handler)
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8080)
        await site.start()

    @routes.get('/health')
    async def health_check(request):
        return web.json_response({'status': 'ok'})
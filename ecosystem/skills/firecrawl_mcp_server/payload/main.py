import asyncio
from firecrawl_mcp_server import FireCrawlMCP

async def main():
    server = FireCrawlMCP()
    await server.start()

if __name__ == '__main__':
    asyncio.run(main())
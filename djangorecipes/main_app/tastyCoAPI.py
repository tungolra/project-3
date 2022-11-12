import aiohttp
import asyncio
import environ

env = environ.Env()
environ.Env.read_env()

URL_BASE = env('TASTYCO_BASE_URL')
API_HOST = env("TASTYCO_HOST")
API_KEY = env("TASTYCO_KEY")

HEADERS = {
    "X-RapidAPI-Key" : API_KEY,
    "X-RapidAPI-Host" : API_HOST
}

async def API_HIT(session, url, query=None):
    
    async with session.get(url) as resp:
        res = await resp.json()
        print (res)
        return res

async def initialize_Session():
    pass
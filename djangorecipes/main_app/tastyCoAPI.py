from requests_threads import AsyncSession
from requests import Session
import asyncio

URL = "https://tasty.p.rapidapi.com/recipes/auto-complete"
QUERY = {
    "prefix" : "chicken soup"
}

HEADERS = {
    "X-RapidAPI-Key" : "a9b8732634mshd9c5ade8ea5bfdap16b3c9jsn4296560a02db",
    "X-RapidAPI-Host" : "tasty.p.rapidapi.com"
}

session = AsyncSession(n=100)

async def _main():
    print("main1:")
    rs = []
    for _ in range(1):
        resp = await session.request("GET", URL, headers = HEADERS, params=QUERY)
        rs.append(resp.text)
    print(rs[0])

res = session.run(_main)    

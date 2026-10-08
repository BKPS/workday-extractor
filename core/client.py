import aiohttp


class AsyncWorkdayClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=60),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )

    async def post(self, path: str, json: dict):
        url = f"{self.base_url}{path}"
        async with self.session.post(url, json=json) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def get(self, path: str, params: dict | None = None):
        url = f"{self.base_url}{path}"
        async with self.session.get(url, params=params or {}) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def close(self):
        await self.session.close()

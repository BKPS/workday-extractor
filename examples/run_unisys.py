import asyncio
from tenants import unisys
from pipeline.extract_universal import extract_tenant
from playwright.token_unisys import get_token_unisys

async def main():
    token = await get_token_unisys()
    jobs = await extract_tenant(unisys, token)
    print(f"Total de vagas Unisys: {len(jobs)}")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from core.client import AsyncWorkdayClient
from core.search import facet_search_all
from core.jobs import fetch_job_details


async def extract_tenant(tenant_module, token: str):
    client = AsyncWorkdayClient(tenant_module.BASE_URL, token)

    try:
        job_ids = await facet_search_all(
            client,
            tenant_module.SEARCH_PATH,
            tenant_module.SEARCH_PAYLOAD_BASE,
            page_size=2000,
        )

        if not job_ids:
            return []

        jobs = await fetch_job_details(
            client,
            tenant_module.JOB_PATH_TEMPLATE,
            job_ids,
            concurrency=20,
        )

        return jobs
    finally:
        await client.close()

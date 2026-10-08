import asyncio
from .client import AsyncWorkdayClient


async def _fetch_one_job(
    client: AsyncWorkdayClient,
    job_path_template: str,
    job_id: str,
):
    path = job_path_template.format(job_id=job_id)
    return await client.get(path)


async def fetch_job_details(
    client: AsyncWorkdayClient,
    job_path_template: str,
    job_ids: list[str],
    concurrency: int = 20,
):
    sem = asyncio.Semaphore(concurrency)

    async def wrapped(job_id: str):
        async with sem:
            try:
                return await _fetch_one_job(client, job_path_template, job_id)
            except Exception as e:
                return {"job_id": job_id, "error": str(e)}

    tasks = [wrapped(jid) for jid in job_ids]
    results = await asyncio.gather(*tasks, return_exceptions=False)

    # Filtra exceções inesperadas (se alguma escapar)
    cleaned = []
    for r in results:
        if isinstance(r, Exception):
            cleaned.append({"error": str(r)})
        else:
            cleaned.append(r)

    return cleaned

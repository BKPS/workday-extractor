from .client import AsyncWorkdayClient


async def facet_search_all(
    client: AsyncWorkdayClient,
    search_path: str,
    payload_base: dict,
    page_size: int = 2000,
):
    offset = 0
    job_ids: list[str] = []

    while True:
        payload = payload_base.copy()
        payload["limit"] = page_size
        payload["offset"] = offset

        data = await client.post(search_path, json=payload)

        # Alguns tenants retornam "total" explícito
        total = data.get("total")
        if total == 0:
            break

        postings = (
            data.get("jobPostings")
            or data.get("searchResult")
            or data.get("items")
            or []
        )

        ids = [
            p.get("id") or p.get("jobId")
            for p in postings
            if p.get("id") or p.get("jobId")
        ]

        if not ids:
            break

        job_ids.extend(ids)
        offset += page_size

    return job_ids

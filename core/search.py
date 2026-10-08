def facet_search_all(client, search_path, payload_base, page_size=2000):
    offset = 0
    job_ids = []

    while True:
        payload = payload_base.copy()
        payload["limit"] = page_size
        payload["offset"] = offset

        data = client.post(search_path, json=payload)

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

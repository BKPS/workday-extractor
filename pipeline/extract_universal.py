from core.client import WorkdayClient
from core.search import facet_search_all
from core.jobs import fetch_job_details

def extract_tenant(tenant, token):
    client = WorkdayClient(tenant.BASE_URL, token)

    job_ids = facet_search_all(
        client,
        tenant.SEARCH_PATH,
        tenant.SEARCH_PAYLOAD_BASE,
        page_size=2000,
    )

    jobs = fetch_job_details(
        client,
        tenant.JOB_PATH_TEMPLATE,
        job_ids,
    )

    return jobs

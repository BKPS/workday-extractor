def fetch_job_details(client, job_path_template, job_ids):
    jobs = []
    for job_id in job_ids:
        path = job_path_template.format(job_id=job_id)
        data = client.get(path)
        jobs.append(data)
    return jobs

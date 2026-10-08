from tenants import unisys
from pipeline.extract_universal import extract_tenant
from playwright.token_unisys import get_token_unisys

token = get_token_unisys()
jobs = extract_tenant(unisys, token)

print(f"Total de vagas Unisys: {len(jobs)}")

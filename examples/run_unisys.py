import asyncio
from tenants import unisys
from pipeline.extract_universal import extract_tenant
from playwright.token_unisys import get_token_unisys


async def main():
    token = await get_token_unisys()
    jobs = await extract_tenant(unisys, token)
    print(f"Total de vagas Unisys: {len(jobs)}")

    # Exemplo de inspeção de uma vaga
    if jobs:
        first = jobs[0]
        print("Primeira vaga (chave principais):")
        for k in list(first.keys())[:10]:
            print(f"  {k}: {first[k]}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print("Erro na execução:", e)

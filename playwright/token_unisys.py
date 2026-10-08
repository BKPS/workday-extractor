from playwright.async_api import async_playwright

UNISYS_URL = "https://unisys.wd5.myworkdayjobs.com/en-US/ExternalCareerSite"

async def get_token_unisys() -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(UNISYS_URL, wait_until="networkidle")
        token = await page.evaluate("window.workday.token")
        await browser.close()
        return token

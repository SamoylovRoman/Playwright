from colorama.win32 import winapi_test
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://granit-elit.ru/pamyatniki-iz-granita/")
        await page.screenshot(path = "screenshot/screen_2.png")
        await browser.close()


asyncio.run(main())
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://granit-elit.ru/")
    # page.get_by_role("button", name="ПОКАЗАТЬ ВСЕ МОДЕЛИ").click()
    page.locator("text=Показать все модели").click()
    page.screenshot(path="screenshot/homepage.png")

    page.locator("#div_search").get_by_placeholder("Поиск товара по каталогу").fill("памятник прямой")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshot/homepage.png")
    browser.close()

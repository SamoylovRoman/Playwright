import re
from time import sleep

from playwright.sync_api import Page, expect, Route, sync_playwright


def test_request(page: Page):
    # лог всех request (включая post_data)
    page.on("request", lambda req: print("REQ:", req.method, req.url, "BODY:", req.post_data))

    # регистрируем роут (до навигации)
    def change_request(route):
        req = route.request
        print("ROUTE INTERCEPT:", req.method, req.url)
        print("route.request.post_data:", req.post_data)
        route.continue_()

    page.route(re.compile("/login"), change_request)
    page.goto("https://deutsch-vorbereitung.com/login.html")

    page.get_by_role("button", name="Alle akzeptieren").click()
    page.locator("xpath=/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/button[1]/p").click()
    page.locator("#email").fill("r.v.samoylov@yandex.ru")
    page.locator("#password").fill("qwerty12345")
    page.locator("xpath=/html/body/section/div/div/form/input[1]").click()
    expect(page.get_by_role("button", name="Abmelden")).to_be_visible()
    sleep(5)


def run_cdp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context()
        page = ctx.new_page()

        client = ctx.new_cdp_session(page)
        client.send("Network.enable")

        def on_request_will_be_sent(params):
            req = params.get("request", {})
            method = req.get("method")
            url = req.get("url")
            postData = req.get("postData")   # <- здесь точно будет тело, если есть
            print("CDP request:", method, url)
            print("    postData:", postData)

        client.on("Network.requestWillBeSent", on_request_will_be_sent)

        # Доп. лог Playwright (для сравнения)
        page.on("request", lambda r: print("PW req:", r.method, r.url, "post_data:", r.post_data))

        page.goto("https://deutsch-vorbereitung.com/login.html")
        page.get_by_role("button", name="Alle akzeptieren").click()
        page.locator("xpath=/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/button[1]/p").click()
        page.locator("#email").fill("r.v.samoylov@yandex.ru")
        page.locator("#password").fill("qwerty12345")
        page.locator("xpath=/html/body/section/div/div/form/input[1]").click()

        page.wait_for_timeout(5000)
        browser.close()
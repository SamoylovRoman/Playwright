import re
from time import sleep

from playwright.sync_api import Page, expect, Route


def test_request(page: Page):

    def change_request(route: Route):
        data = route.request.post_data
        print(data)
        route.continue_()

    page.goto("https://www.mediamarkt.de/")
    # page.on("request", lambda req: print("REQ", req.method, req.url))
    page.locator("#pwa-consent-layer-accept-all-button").click()
    page.get_by_role("button", name="Mein Konto").click()
    page.fill('#userName', "test@example.com")
    page.locator("#password").fill("1245qwerty")
    page.get_by_role("button", name="Einloggen").click()

    page.route(re.compile("/authentication"), change_request)

    # page.get_by_role("button", name="Alle zulassen").click()
    # page.locator("xpath=/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/button[1]/p").click()
    # page.locator("#email").fill("r.v.samoylov@yandex.ru")
    # page.locator("#password").fill("qwerty12345")
    # page.locator("xpath=/html/body/section/div/div/form/input[1]").click()
    # expect(page.get_by_role("button", name="Abmelden")).to_be_visible()

    page.pause()
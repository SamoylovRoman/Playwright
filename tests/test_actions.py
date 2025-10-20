from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.goto("https://granit-elit.ru/pamyatniki-iz-granita/")

    page.locator("#v-1000110001").click()
    page.locator("#v-1000110002").click()
    page.locator("#v-1000110001").click()
    page.locator("#v-1000110002").click()
    page.locator("#v-1000110001").click()
    expect(page).to_have_url("https://granit-elit.ru/pamyatniki-iz-granita/pamyatniki-ekonomnye/")
    # expect(page).to_have_url("https://granit-elit.ru/search/?search=%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D0%B9")

    page.pause()
from playwright.sync_api import Page, expect


def test_main_page_title(page: Page):
    page.goto("https://granit-elit.ru/")
    assert page.title() == "Купить памятники из гранита на могилу в Новосибирске - Гранит-Элит"


def test_pamyatniki_page(page:Page):
    page.goto("https://granit-elit.ru/")
    page.locator("xpath=/html/body/header/div[2]/div/div[1]/div/a[1]").click()
    # assert page.title() == "Каталог гранитных памятников на могилу в Новосибирске с ценами - Гранит-Элит"
    expect(page).to_have_title("Каталог гранитных памятников на могилу в Новосибирске с ценами - Гранит-Элит")


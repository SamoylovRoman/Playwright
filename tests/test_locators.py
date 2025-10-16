from playwright.sync_api import Page, expect


def test_locator_role(page: Page):
    page.goto("https://granit-elit.ru/")
    page.get_by_role("link", name="НАШ КОЛЛЕКТИВ").click()
    expect(page).to_have_title("Наш коллектив")
    # page.get_by_role("link", name="ПАМЯТНИКИ").click()
    # expect(page.get_by_text("Памятники из гранита")).to_be_visible()


def test_locator_role_button(page: Page):
    page.goto("https://granit-elit.ru/")
    page.get_by_role("button", name="Везде").click()
    expect(page.locator("#div_search").get_by_text("Вазы, таблички, другое")).to_be_visible()
    # expect(page).to_have_title("Каталог гранитных памятников на могилу в Новосибирске с ценами - Гранит-Элит")


def test_locator_placeholder(page:Page):
    page.goto("https://granit-elit.ru/")
    page.locator("#div_search").get_by_placeholder("Поиск товара по каталогу").fill("памятник прямой")
    page.keyboard.press("Enter")
    expect(page.locator("#content").get_by_text("Поиск - памятник прямой")).to_be_visible()


def test_locator_alttext(page:Page):
    page.goto("https://granit-elit.ru/our-team")
    page.get_by_alt_text("Гранит-элит").click()
    expect(page).to_have_url("https://granit-elit.ru/")


def test_locator_xpath(page:Page):
    page.goto("https://granit-elit.ru/")
    # expect(page.locator("xpath=/html/body/footer/div/div[2]/div[1]/div/a[1]")).to_be_visible()
    expect(page.locator("a[href='https://vk.com/granitelit']")).to_be_visible()
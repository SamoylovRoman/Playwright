import pytest
from playwright.sync_api import Page


#@pytest.fixture(autouse=True)
def open_main_page(page: Page):
    page.goto("https://granit-elit.ru/")
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


def test_title(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
def test_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")  # вводим логин
    page.fill("#password", "SuperSecretPassword!")  # вводим пароль
    page.click("button[type='submit']")  # кликаем кнопку
    # assert page.url == "https://the-internet.herokuapp.com/secure"
    assert "/secure" in page.url
    # используй: page.url

def test_login_success_message(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    # проверь что на странице есть текст "You logged into a secure area!"
    assert "You logged into a secure area!" in page.inner_text("div.flash")
    # используй: page.inner_text("div.flash")
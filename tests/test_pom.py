import allure
from pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.title("Успешный вход в систему")
def test_login_success(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username='tomsmith', password='SuperSecretPassword!')
    assert "/secure" in page.url

@allure.feature("Авторизация")
@allure.title("Вход с неверным паролем")
def test_login_fail(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username='tomsmith', password='!')
    assert 'Your password is invalid!' in login_page.get_flash_message()

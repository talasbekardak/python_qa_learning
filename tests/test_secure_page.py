import allure
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

@allure.feature("Защищённая страница")
@allure.title("После входа открывается защищённая страница")
def test_get_heading(page):
    login_page = LoginPage(page)
    secure = SecurePage(page)
    login_page.open()
    login_page.login('tomsmith', 'SuperSecretPassword!')
    assert "/secure" in page.url
    assert "Secure Area" in secure.secure_text()

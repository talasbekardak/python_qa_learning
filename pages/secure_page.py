import allure

class SecurePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Открываю защищённую страницу")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/secure")

    @allure.step("Получаю текст защищённой страницы")
    def secure_text(self):
        return self.page.text_content("div.example")

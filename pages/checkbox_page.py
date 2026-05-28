import allure

class CheckboxPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Открываю страницу чекбоксов")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    @allure.step("Проверяю состояние чекбокса #{n}")
    def is_checked(self, n):
        return self.page.is_checked(f"input[type='checkbox']:nth-of-type({n})")

    @allure.step("Кликаю на чекбокс #{n}")
    def click_checkbox(self, n):
        self.page.click(f"input[type='checkbox']:nth-of-type({n})")

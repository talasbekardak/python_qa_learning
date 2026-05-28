import allure

class LoginPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Открываю страницу логина")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    @allure.step("Ввожу логин '{username}' и пароль, нажимаю войти")
    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")

    @allure.step("Получаю текст flash-сообщения")
    def get_flash_message(self):
        return self.page.inner_text("div.flash")

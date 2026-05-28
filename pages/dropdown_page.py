import allure
class DropdownPage:
    def __init__(self, page):
        self.page = page
    @allure.step("Открываю страницу дропдауна")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")
    @allure.step("Выбираю опцию {value}")
    def select_option(self, value):
        self.page.select_option("#dropdown", value)
    @allure.step("Получаю текст выбранной опции")
    def get_selected_text(self):
        return self.page.locator("#dropdown option:checked").inner_text()


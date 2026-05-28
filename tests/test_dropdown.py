import allure
from pages.dropdown_page import DropdownPage

@allure.feature("Дропдаун")
@allure.title("Открытие страницы с дропдауном")
def test_opens_dropdown_page(page):
    dropdown = DropdownPage(page)
    dropdown.open()

@allure.feature("Дропдаун")
@allure.story("Выбор опции")
@allure.title("Выбор Option 1 в дропдауне")
def test_opens_dropdown_page_with_options(page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_option("Option 1")
    assert "Option 1" in dropdown.get_selected_text()

@allure.feature("Дропдаун")
@allure.story("Выбор опции")
@allure.title("Выбор Option 2 в дропдауне")
def test_opens_dropdown_page_with_option(page):
    dropdown = DropdownPage(page)
    dropdown.open()
    dropdown.select_option("Option 2")
    assert "Option 2" in dropdown.get_selected_text()



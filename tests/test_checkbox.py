import allure
from pages.checkbox_page import CheckboxPage

@allure.feature("Чекбоксы")
@allure.title("Страница чекбоксов открывается")
def test_open_success(page):
    checkbox = CheckboxPage(page)
    checkbox.open()
    assert "the-internet.herokuapp.com/checkboxes" in page.url

@allure.feature("Чекбоксы")
@allure.story("Клик по чекбоксу")
@allure.title("Клик по чекбоксу #1 активирует его")
def test_click_checkbox(page):
    checkbox = CheckboxPage(page)
    checkbox.open()
    checkbox.click_checkbox("1")
    assert checkbox.is_checked("1") == True
#source .venv/bin/activate && pytest tests/test_checkbox.py -v --alluredir=allure-results

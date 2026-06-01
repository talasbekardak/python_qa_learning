# Конспект — Этап 4: Page Object Model (POM)

## Что такое POM

Паттерн проектирования тестов. Каждая страница сайта — отдельный класс. Тесты не знают про селекторы — они просто вызывают методы страницы.

**Проблема без POM:**
Селекторы разбросаны по всем тестам. Поменялся один элемент на сайте — правишь в 10 местах.

**Решение с POM:**
Селектор живёт в одном месте (в классе страницы). Поменялся элемент — правишь в одном месте.

---

## Структура проекта с POM

```
pages/
  login_page.py       # класс LoginPage
  checkbox_page.py    # класс CheckboxPage
  dropdown_page.py    # класс DropdownPage
  secure_page.py      # класс SecurePage
tests/
  conftest.py         # общие fixtures
  test_pom.py         # тесты используют классы из pages/
```

---

## Как выглядит Page Object класс

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page          # сохраняем объект страницы Playwright

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")

    def get_flash_message(self):
        return self.page.inner_text("div.flash")
```

Правило: класс страницы **не содержит assert**. Только действия и получение данных. Assert — в тесте.

---

## Как выглядит тест с POM

```python
# tests/test_pom.py
from pages.login_page import LoginPage

def test_login_success(page):
    login_page = LoginPage(page)   # создаём объект страницы
    login_page.open()              # открываем страницу
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "/secure" in page.url   # проверяем результат

def test_login_fail(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "!")
    assert "Your password is invalid!" in login_page.get_flash_message()
```

---

## conftest.py — общие fixtures

Файл с fixtures, которые доступны всем тестам в папке. pytest подхватывает его автоматически — импортировать не нужно.

```python
# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page        # передаём page в тест
        browser.close()   # выполнится после теста
```

---

## Примеры из проекта

### CheckboxPage
```python
class CheckboxPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def is_checked(self, n):
        return self.page.is_checked(f"input[type='checkbox']:nth-of-type({n})")

    def click_checkbox(self, n):
        self.page.click(f"input[type='checkbox']:nth-of-type({n})")
```

### DropdownPage
```python
class DropdownPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def select_option(self, value):
        self.page.select_option("#dropdown", value)

    def get_selected_text(self):
        return self.page.locator("#dropdown option:checked").inner_text()
```

---

## Итог: зачем POM

| Без POM | С POM |
|---------|-------|
| Селекторы в тестах | Селекторы в классах страниц |
| Изменение → правка в 10 местах | Изменение → правка в 1 месте |
| Тесты длинные и повторяются | Тесты короткие и читаемые |

# Конспект — Этап 3: UI-тесты с Playwright

### Основные команды
```python
page.goto(url)               # открыть страницу
page.title()                 # заголовок вкладки (<title>)
page.url                     # текущий URL
page.fill(selector, text)    # ввести текст в поле
page.click(selector)         # кликнуть по элементу
page.inner_text(selector)    # получить текст элемента
```

### Селекторы — как найти элемент
| HTML | Селектор | Пример |
|------|----------|--------|
| `id="username"` | `#id` | `#username` |
| `class="flash"` | `.class` | `div.flash` |
| `type="submit"` | `[attr='val']` | `button[type='submit']` |
| текст элемента | `text=...` | `text=Login` |

**Как найти селектор:** открой сайт в Chrome → правой кнопкой на элемент → Inspect → смотри HTML.

### Пример теста без fixture
```python
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")
        assert "/secure" in page.url
        assert "You logged into a secure area!" in page.inner_text("div.flash")
        browser.close()
```

### Fixtures
Fixture — способ вынести повторяющийся код (запуск браузера, подключение к БД и т.д.) в одно место. Тест просто получает готовый объект через аргумент.

- `@pytest.fixture` — декоратор, помечает функцию как fixture
- `yield` — передаёт объект в тест; код после `yield` выполняется после теста (cleanup)
- тест получает fixture автоматически — просто добавь имя fixture как аргумент функции

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page        # передаём page в тест
        browser.close()   # выполнится после теста

def test_title(page):     # page приходит из fixture автоматически
    page.goto("https://example.com")
    assert "Example" in page.title()

def test_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    assert "/secure" in page.url
```

# Конспект — Этап 2: API-тесты с requests

### Что такое API
Интерфейс через который программы общаются через интернет. Мы отправляем HTTP-запросы и проверяем ответы.

### Основные типы запросов
- `GET` — получить данные
- `POST` — отправить / создать данные

### response — объект ответа
```python
response.status_code  # код ответа: 200 = ок, 201 = создано, 404 = не найдено
response.json()       # тело ответа в виде словаря
```

### Примеры тестов
```python
import requests

# GET — проверка статуса и наличия ключа
def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    assert response.status_code == 200
    assert "name" in response.json()

# POST — создание ресурса
def test_create_post():
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "test", "body": "hello", "userId": 1},
        timeout=10
    )
    assert response.status_code == 201
    assert "id" in response.json()

# Проверка конкретных значений
def test_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "Bret"
```

### timeout
Всегда добавляй `timeout=10` — если сервер не ответил за 10 секунд, тест сразу падает с ошибкой вместо бесконечного ожидания.

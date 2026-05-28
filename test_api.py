import requests


def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    assert response.status_code == 200
    assert "name" in response.json()

def test_create_post():
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "test", "body": "hello", "userId": 1},
        timeout=10
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "Bret"

# Конспект — Этап 1: pytest

### Что такое тест
Функция, которая проверяет что код работает правильно. Если проверка не прошла — тест падает и сразу видно что сломалось.

### assert
Утверждение. Если условие `False` — бросает ошибку:
```python
assert 2 + 2 == 4   # ок
assert 2 + 2 == 5   # AssertionError — тест упал
```

### pytest.raises
Проверяет что код намеренно бросает исключение:
```python
with pytest.raises(ValueError):
    acc.withdraw(999)  # ожидаем ошибку — тест пройдёт
```

### @pytest.mark.parametrize
Запускает один тест с разными наборами данных. Вместо 10 одинаковых функций — одна:
```python
@pytest.mark.parametrize("a, b, result", [
    (2, 3, 6),
    (5, 2, 10),
])
def test_multiply(a, b, result):
    assert multiply(a, b) == result
# pytest запустит этот тест 2 раза с разными данными
```

### if __name__ == "__main__"
Код внутри запускается только при прямом запуске файла, но не при импорте.
Важно когда pytest импортирует твои файлы — без этого весь код в файле выполнится при импорте:
```python
if __name__ == "__main__":
    acc = BankAccount(0)
    acc.deposit(100)
    print(acc.balance())
```

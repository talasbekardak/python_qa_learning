# Конспект — Этап 0: Python-фундамент

### Функции
Блок кода с именем, который можно вызывать много раз:
```python
def multiply(a, b):
    return a * b

multiply(3, 4)  # вызов → вернёт 12
```

### Списки
Упорядоченная коллекция элементов. Можно перебирать циклом, фильтровать:
```python
numbers = [1, 2, 3]
for n in numbers:
    print(n)
```

### Словари
Коллекция пар "ключ: значение":
```python
user = {"name": "Alice", "age": 30}
user["name"]  # → "Alice"
```

### Классы
Шаблон для создания объектов со своими данными и методами.
- `self` — это сам объект
- `__init__` — запускается при создании объекта

```python
class BankAccount:
    def __init__(self):
        self._balance = 0   # у каждого объекта свой баланс

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def balance(self):
        return self._balance
```

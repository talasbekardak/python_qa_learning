class BankAccount:
    def __init__(self, balance):
        self._balance = 0
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if self._balance - amount < 0 :
            raise ValueError("Недостаточно средств")
        self._balance -= amount
    def balance(self):
        return self._balance
if __name__ == "__main__":
    acc = BankAccount(0)
    acc.deposit(100)
    acc.deposit(50)
    print(acc.balance())
    acc.withdraw(30)
    print(acc.balance())
    acc.withdraw(200)
    print(acc.balance())

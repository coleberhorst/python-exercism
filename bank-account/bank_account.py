from threading import Lock


class BankAccount(object):
    def __init__(self):
        self.balance = None
        self._lock = Lock()

    def get_balance(self):
        with self._lock:
            if self.balance == None:
                raise ValueError("Account is not open.")
            return self.balance

    def open(self):
        with self._lock:
            if self.balance != None:
                raise ValueError("Cannot open already open account.")
            self.balance = 0

    def deposit(self, amount):
        with self._lock:
            if amount < 0:
                raise ValueError("Deposits cannot be negative.")
            elif self.balance == None:
                raise ValueError("Cannot deposit into a closed account.")
            self.balance += amount

    def withdraw(self, amount):
        with self._lock:
            if self.balance == None:
                raise ValueError("Cannot withdraw from closed account.")
            elif amount > self.balance:
                raise ValueError("Not enough money for withdrawal.")
            elif amount < 0:
                raise ValueError("Withdrawals cannot be negative.")
            self.balance -= amount

    def close(self):
        with self._lock:
            if self.balance == None:
                raise ValueError("Account already closed.")
            self.balance = None

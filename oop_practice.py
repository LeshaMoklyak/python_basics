from typing import List, Dict


class BankAccount:
    def __init__(self, account_holder: str, balance: int):
        self.account_holder = account_holder
        self.balance = balance

        self._transactions = []

    def deposit(self, amount: int) -> int:
        if amount <= 0: 
            raise ValueError('Только положительные суммы')
        
        self.balance = self.balance + amount
        self._transactions.append({
            'type': 'deposit',
            'amount': amount,
            'balance': self.balance
        })
        return self.balance
    
    def withdraw(self, amount: int) -> int:
        if amount < 0: 
            raise ValueError('Вывести можно только положительную сумму')
        
        if amount > self.balance:
            raise ValueError('Недостаточно средств')
        
        self.balance = self.balance - amount
        self._transactions.append({
            'type': 'withdraw',
            'amount': amount,
            'balance': self.balance
        })
        return self.balance
    
    def get_transactions(self) -> List[Dict]:
        return self._transactions
    
    def get_balance(self) -> int:
        return self.balance
    
    def __str__(self) -> str:
        return f"Счет {self.account_holder}: {self.balance} руб."
    

account = BankAccount("Иван Иванов", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300
print(account.get_transactions())
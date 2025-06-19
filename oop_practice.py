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
    

class Product:
    def __init__(self, name: str, price: float, quant: int):
        if price <= 0:
            raise ValueError('Цена должна быть положительным числом')
        if quant <= 0:
            raise ValueError('Количество должно быть положительным числом')
        
        self.name = name
        self.price = price
        self.quant = quant
    
    def is_available(self) -> bool:
        return self.quant > 0

    def change_quantity(self, amount: int) -> int: 
        if amount > self.quant:
            raise ValueError(f'Доступно для покупки только  единиц {self.quant} товара')
        if amount <= 0:
            raise ValueError('Вы можете купить только положительно число товара')
        if not self.is_available():
            raise ValueError('Товар закончился')
        self.quant = self.quant - amount
        return self.quant

    def add_quantity(self, amount: int) -> int:
        if amount < 0:
            raise ValueError('количество должно быть положительным')
        self.quant = self.quant + amount
        return self.quant

    def __str__(self):
        return f"Название {self.name}, Цена: {self.price}, Остаток: {self.quant}"


class User:
    def __init__(self, user: str, email: str):
        self.user = user 
        self.email = email

        self.card: List[Dict] = []
        self.purchase_history: List[Dict] = []

    def add_to_cart(self, product: Product, quant: int) -> None:

        if not product.is_available():
            raise ValueError('Товар закончился')
        if quant < 0: 
            raise ValueError('Вы можете купить только положительно число товара')
        if quant > product.quant:
            raise ValueError(f'Недостаточно товара. Доступно {product.quant}')
        
        for item in self.card:
            if item['product'].name == product.name:
                item['quantity'] += quant
                break
        else:
            self.card.append({'product': product, 'quantity': quant})

    def remove_to_cart(self, product: Product, quant: int) -> None:
        if not self.card: 
            raise ValueError('Корзина пуста')
        
        for item in self.card:
            if not item['product'].name== product.name:
                raise ValueError('Товар отсутствует у вас в корзине')
            
            if item['quantity'] <= product.quant:
                self.card.remove(item)
                
            if item['quantity'] > product.quant:
                item['quantity'] -= quant
                
                  

    def __str__(self):
        return f'Пользователь: {self.user} Емаил: {self.email} Товаров: {len(self.card)}'
    

prod1 = Product('arbuz', 25, 10)
user1 = User('alex', 'email123')
print(prod1)

user1.add_to_cart(prod1, 2)
print(user1)
user1.remove_to_cart(prod1,2)
print(user1)
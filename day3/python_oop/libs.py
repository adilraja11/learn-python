class BankAccount:
    def __init__(self, username, balance = 0):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited!")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawed!")

    def check_balance(self):
        print(f"Account: {self.username}, Balance: {self.balance}")

class Member:
    def __init__(self, name):
        self.name = name
        self.is_active = True
        
    def deactivate(self):
        self.is_active = False
        
    def activate(self):
        self.is_active = True
        
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        
    def register_member(self, member: Member):
        self.members.append(member)
        
    def get_active_members(self):
        active_members = []
        for member in self.members:
            if member.is_active:
                active_members.append(member)
                
        return active_members
class LunchCard:
    def __init__(self, balance: float):
        self.balance = float(balance)
    
    def eat_lunch(self):
        if self.balance < 2.60:
            return
        self.balance -= 2.60
        
    def eat_special(self):
        if self.balance < 4.60:
            return
        self.balance -= 4.60
        
    def deposit_money(self, deposit):
        if deposit <= 0:
            raise ValueError("You cannot deposit an amount of money less than or equal to zero")
        self.balance += deposit
        
    def __str__(self):
        return f"The balance is {round(self.balance, 1)} euros"

Peter = LunchCard(20)
Grace = LunchCard(30)

Peter.eat_special()
Grace.eat_lunch()

print(f"Peter: {Peter}")
print(f"Grace: {Grace}")

Peter.deposit_money(20)
Grace.eat_special()

print(f"Peter: {Peter}")
print(f"Grace: {Grace}")

Peter.eat_lunch()
Peter.eat_lunch()
Grace.deposit_money(50)

print(f"Peter: {Peter}")
print(f"Grace: {Grace}")

# tek altçizgi (_) protacted yapar
#çift alt çizgi (__) private yapar

class BankAccount:
    def __init__(self,initial_balance):
        self.__balance = initial_balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Yetersiz Bakiye")

    def get_balance(self):
        return self.__balance

account1 = BankAccount(1000)

print(account1.get_balance()) #Bakiye kontrol

account1.deposit(500) #para yatırma

print(account1.get_balance())

account1.withdraw(100) #para çekme

print(account1.get_balance())

account1.withdraw(2500) #hatalı para çekme


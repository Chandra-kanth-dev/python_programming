class BankAccount:
    __balance=0
    def __init__(self):
        pass
    def deposit(self,amount):
       self. __balance+=amount
    def withdraw(self,amt):
        if self.__balance<amt:
            print("insufficient balance")
        else:
            self.__balance-=amt
    def get_balance(self):
        print("available balance",self.__balance)
bankacc= BankAccount()
bankacc.deposit(5000)
bankacc.withdraw(2000)
bankacc.get_balance()



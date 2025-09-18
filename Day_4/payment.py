class Payment:
    def pay(self,amount):
        print(amount, "paid")
class CashPayment(Payment):
    def pay(self,amount):
        print("paid ",amount,"in cash")

class CardPayment(Payment):
    def pay(self,amount):
        print("paid ",amount,"through debit/credit card")

class UPIPayment(Payment):
    def pay(self,amount):
        print("paid ",amount,"through upi")
l = [
    CashPayment(),
    CardPayment(),
    UPIPayment(),
]
for i in l :
    i.pay(10000000)
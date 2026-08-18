# Create Account class with 2 attributes - balance and acc no.
# Create methods for debit, credit, and printing the balance.

class Account:
    def __init__(self, acc_no, balAmt):
        self.acc_no = acc_no
        self.balAmt = balAmt

    def debit(self, debAmt):
        self.debAmt = debAmt
        print(self.debAmt, "was Debited to your Account.")

    def credit(self, creAmt):
        self.creAmt = creAmt
        print(self.creAmt, "was Credited from your Account.")

    def balance(self):
        print("Balance Amount:", self.balAmt + self.debAmt - self.creAmt)

acc1 = Account(321654, 1000)
acc1.debit(200)
acc1.credit(0)
acc1.balance()
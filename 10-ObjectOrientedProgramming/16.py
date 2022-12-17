class BANK:
    def __init__(self,number):
        self.balance=0
        self.number=number
    def deposit(self,amount):
        self.amountplus=amount
        self.balance+=self.amountplus
    def withdraw(self,amount):
        self.amountminus=amount
        if self.amountminus<self.balance or self.amountminus==self.balance:
            self.balance-=self.amountminus
        elif self.amountminus>self.balance:
            print('Insufficient funds on thr account')
    def display(self):
        print(f'Bank Account No:{self.number}\nBalance:PLN {self.balance}')

acc=BANK('12 3456 5555 9090 1111 0000 7722')    
acc.display()  
acc.deposit(25.30)
acc.display()
acc.withdraw(31.70)
acc.display()
acc.deposit(14)
acc.display()
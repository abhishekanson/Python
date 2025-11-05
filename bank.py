class BankAccount():
    def __init__(self,accountholder,balance=0.0):
        self.accountholder=accountholder
        self.balance=balance
    
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print(f"{amount} credited to your account")
        else:
            print("Deposit amount should be greater than zero")
    
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficient Fund in your account")
        elif (amount <= 0):
            print("Withdrawal amount should be greater than zero")
        else:
            self.balance-=amount
            print(f"{amount} debited from your account")
    
    def check_balance(self):
        print(f"Your current balance is {self.balance}")

    def __str__(self):
        return f"Account holder: {self.accountholder}, Balance: {self.balance}"
    

name=input("Enter account holder name: ")
initial_balance=float(input("Enter initial deposit amount: "))
account=BankAccount(name,initial_balance)
while True:
    print("\n====Bank Menu====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice=int(input("Enter your choice (1-5): "))

    if choice==1:
        amount=float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice==2:
        amount=float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice==3:
        account.check_balance()
    
    elif choice==4:
        print(account)

    elif choice==5:
        print("Thank You")
        break

    else:
        print("Invalid input")
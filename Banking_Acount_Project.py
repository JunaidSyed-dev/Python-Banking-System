
# Project Simulating Banking System using OOPS Concept :

from abc import ABC , abstractmethod 

class Account (ABC) :

    @abstractmethod
    def get_balance(self) :
        pass

    @abstractmethod
    def deposit(self,amount) :
        pass 

    @abstractmethod
    def withdraw(self,amount) :
        pass


class SavingsAccount (Account) :

    def __init__(self) :
        self.__balance = 500 
    
    def get_balance(self) :
        return self.__balance
    
    def withdraw(self,amount) :
        if (amount > 0) and (self.__balance - amount >= 500) :
            self.__balance -= amount 
            print(f"An Amount of rupees {amount} /- has been debited from your Account.")

        else :
            print("Invalid Amount , Try Again ! ")
    def deposit(self,amount) :
        if (amount > 0 ) :
            self.__balance += amount 
            print(f"An Amount of rupees {amount} /- has been credited to your Account.")
        else :
            print("Invalid Amount !")
  

class CurrentAccount(Account) :

    def __init__(self):
        self.__balance = 0
        self.overdraft = 5000

    def get_balance(self) :
        return self.__balance 
    
    def withdraw(self,amount) :
        if (amount <= 0) :
            print("Invalid Amount !")
            

        elif (amount <= self.__balance) :
            self.__balance -= amount
            print(f"Amount of Rupees {amount} has been debited from Your Account.")


        else :
            print("Requested Amount is Greater than the Available Balance ! \nTry using Overdraft_Withdrawal if U need !")

    
    
    
    def overdraft_withdrawal(self,amount):
        if (amount <= 0 ) :
            print("Invalid Amount !")

        elif (amount <= self.overdraft) :
            self.overdraft -= amount
            print(f"Amount of Rupees {amount} has been debited from Overdraft_Withdrawal from Account.")

        else :
            print("The Requested amount is greater than the available Overdraft Balance !")

    def deposit(self,amount) :
        if (amount <= 0) :
            print("Enter a valid Amount !")
        
        else :
            self.__balance += amount
            print(f"An Amount of rupees {amount} /- has been credited to your Account .")


s1 = SavingsAccount() # This is the object for the Savings Account

s1.deposit(5000)        # Testing Deposit in Savings Account 
s1.withdraw(2000)       # Testing Withdrawal in Savings Account 

print(s1.get_balance()) # Printing Balance of Savings Account


c1 = CurrentAccount()   # This is the object for the Current Account

c1.deposit(1000)        # Testing Deposit in Current Account 
c1.withdraw(500)        # Testing withdrawal in Current Account

print(c1.get_balance())  # Printing Balance of Current Account

c1.overdraft_withdrawal(1000)         # Testing Overdraft withdrawal for Business Accounts


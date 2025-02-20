
class BankAccount():
    def __init__(self,AccountNumber,Balance):
        self.AccountNumber = AccountNumber
        self.__Balance = Balance 

    def Deposit(self,Amount):
        self.__Balance += Amount
        return print("New balance is:",self.__Balance)
    
    def Withdraw(self,Amount):
        if Amount > self.__Balance:
            return print("Insuficient Funds")
        self.__Balance -= Amount
        return print("Withdraw succssful, New balance is: ",self.__Balance)

    def Check_Balance(self):
        return print("Your account balance is: ",self.__Balance)
    
    def my_account(self):
        return print('Your account info is: ',self.AccountNumber)
        

Customer_1= BankAccount(222154965877,100000)

Customer_1.Deposit(12000)
Customer_1.Withdraw(2000000)
Customer_1.Check_Balance()
Customer_1.my_account()
Customer_1.Withdraw(10000)
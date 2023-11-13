class User:
    def __init__ (self,name,age):
        # the User name and age of account 
        self.name = name
        self.age = age
    def displaydetails(self):
        #displays details of account
        print ("Name: " + self.name)
        print ("Age: " + self.age)
class Bank (User):
    def __init__(self,name,age):
        super().__init__ (name,age)
        self.balance = 0 
    def deposit (self,amount):
        self.balance = self.balance + amount
        print (f"New balance is {self.balance}")
def ui (x,age):
    print ('''Enter:
        \033[1m   Account \033[0m
           Details - TO display account details
        \033[1m   Bank \033[0m
           Deposit - To deposit money into bank account
           Withdraw - To withdraw money from bank account
           Display - To display details of your bank account
        \033[1m   Shopping \033[0m
           Purchase - To add an available item to the cart 
           Remove - To remove item from cart
           Checkout - To purchase items
           ''')
    option = input("What do you want to do, " + x.title() + " " )
    user = Bank(x,age)
    if option.lower() == "details":
        user.displaydetails()
        return ui (x,age)
    elif option.lower() == "deposit":
        amount = int(input("How much do we you want to deposit? "))
        if amount < 0:
            print("You can not deposit negative money")
            return ui (x,age)
        else: 
            user.deposit(amount)
    elif option.lower() == "withdraw":
        pass
    elif option.lower() == "display":
        pass
    elif option.lower() == "buy":
        pass
    elif option.lower() == "remove from cart":
        pass
    elif option.lower() == "checkout":
        pass
    else:
        print ("Please enter valid option")
        return ui(x,age)


def logon(x):
    global lockingout
    if lockingout == 3:
        print ("Failed too many times. You have been locked out.")
        quit()
    else:
        if x.lower() == "aidan":
            print ("Welcome, Aidan")
            age = -127
            ui(x,age)
        elif x.lower() == "akhil":
            print ("Welcome, Akhil")
            age = 17
            ui(x,age)
        elif x.lower() == "adam":
            print ("Welcome, Adam")
            age = 1
            ui(x,age)
            
        else:
            print ("You have failed to enter a valid user")
            lockingout = lockingout + 1
            return logon(input ("please enter a name "))
lockingout = 0
logon(input ("Please enter a name "))

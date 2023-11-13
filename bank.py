class User:
    def __init__ (self,name,age):
        # the User name and age of account 
        self.name = name
        self.age = age
    def displaydetails(self):
        #displays details of account
        print (self.name)
        print (self.age)
class Bank (User):
    def __init__(self,name,age):
        super().__init__ (self,name,age)
        self.balance = 0 
    def deposit (self,amount):
        self.balance = self.balance + amount
        print (f"New balance is {self.balance}")
def ui (x,age):
    print (f'''Enter:
           {\033[1m}bank{"\033[0m}
           Deposit - To deposit money into bank account
           Withdraw - To withdraw money from bank account
           Display - To display details of your bank account
           
           
''')
    option = input("What do you want to do, " + x )
    if option.lower() == "deposit":
        pass
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

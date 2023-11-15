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
        super().__init__ (self,name,age)
        pass
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

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
        pass
def logon(x):
    global lockingout
    if lockingout == 3:
        print ("Failed too many times. You have been locked out.")
        quit()
    else:
        if x == "Aidan":
            print ("Welcome, Aidan")
            age = -127
            
        elif x == "Akhil":
            print ("Welcome, Akhil")
            age = 17
        elif x == "Adam":
            print ("Welcome, Adam")
            age = 1
            
        else:
            print ("You have failed to enter a valid user")
            lockingout = lockingout + 1
            return logon(input ("please enter a name "))
lockingout = 0
logon(input ("please enter a name "))

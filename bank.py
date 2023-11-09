class User:
    def __init__ (self,name,age):
        # the User name and age of account 
        self.name = name
        self.age = age
    def displaydetails(self):
        #displays details of account
        print (self.name)
        print (self.age)
def logon(x):
    if lockingout == 3:
        print ("Failed too many times. You have been locked out.")
        quit()
    else:
        if x == "Aidan":
        elif x == "Akhil":
        elif x == "Adam":
name = input ("please enter a name ")
lockingout = 0

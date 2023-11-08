class User:
    def __init__ (self,name):
        # the User name and age of account 
        self.name = name
    def displaydetails(self):
        #displays details of account
        print (self.name)
        print (self.age)
class Aidan(User):
    def __init__(self,name):
        super().__init__(name)
        self.age = -136
class Akhil(User):
    def __init__(self,name):
        super().__init__(name)
        self.age = 17
class Adam(User):
    def __init__(self,name):
        super().__init__(name)
        self.age = 2
def 

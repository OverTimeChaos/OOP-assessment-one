class User:
    def __init__ (self,name,age):
        # the User name and age of account 
        self.name = name
        self.age = age
    def displaydetails(self):
        #displays details of account
        print ("Name: " + self.name.title())
        print ("Age: " + str(self.age))






class Bank (User):
    def __init__(self,name,age):
        #allows perimeters to be inherited also 
        super().__init__ (name,age) 
        self.balance = 0
    def deposit (self,amount):
        #allows user to add money to account
        self.balance = self.balance + amount
        print (f"New balance is {self.balance}")
    def withdraw (self,amount):
        #allows user to redraw money from account
        self.balance = self.balance - amount
    def displaybank (self):
        # display balance
        print ("Balance: " + str(self.balance))





class Product():
    # creates the attributes for products 
    def __init__(self,name,desc,quantity,price):
        self.name = name
        self.desc = desc
        self.quantity = quantity
        self.price = price
    def list(self):
        #lists the products profile
        print (f'''                   \033[1m{self.name}\033[0m
                          {self.desc}
quantity: {self.quantity}
Price: ${self.price}''')
    def reduce(self,amount):
        #checks if amount can be reduced and then reduces the amount if it can
        if self.quantity < amount:
            return print ("Sorry there are no more of this product left")
        else:
            self.quantity = self.quantity - amount
    def increase(self,amount):
          #increases the amount of that product
        self.quantity = self.quantity + amount
computer = Product("Computer","A personal electronic device",15,500)
laptop = Product("Laptop","A portable personal electronic device",5,600)
mouse = Product ("Mouse","A device that allows manipulation of the cursor",50,50)
keyboard = Product ("Keyboard","A device that allows you to type with your device",50,50)
products = [computer,laptop,mouse,keyboard]


        
def ui (x,age,option,user):
    if option.lower() == "details":
        user.displaydetails()
        return options (x,age,user)
    elif option.lower() == "deposit":
        try:
            #checks if the value entered is a integer
            amount = int(input("How much do we you want to deposit? "))
            if amount < 0:
                #checks if the value is above zero and is not negative
                print("You can not deposit negative money")
                return ui (x,age,option,user)
            else: 
                user.deposit(amount)
                return options (x,age,user)
        except ValueError:
            print ("please enter a valid \033[1mNUMBER\033[0m")
            return ui (x,age,option,user)
    elif option.lower() == "withdraw":
        try:
            #checks if the value entered is a integer
            amount = int(input("How much do we you want to deposit? "))
            if amount < 0:
                #checks if the value is above zero and is not negative
                print("You can not withdraw negative money")
                return ui (x,age,option,user)
            elif user.balance < amount:
                #checks if the user had enough money to withdraw
                print ("You can not withdraw that amount of money")
                return ui(x,age,option,user)
            else: 
                user.withdraw(amount)
                return options (x,age,user)
        except ValueError:
            print ("please enter a valid \033[1m   NUMBER \033[0m")
            return ui(x,age,option,user)
    elif option.lower() == "display":
        # displays user's bank details
        user.displaybank()
        return options(x,age,user)
    elif option.lower() == "products":
        #Displays a list of available products 
        print ('''               1 - Computer
               2 - Laptop
               3 - Mouse
               4 - Keyboard''')
        try:
            choose = int (input("Input a valid number "))-1
            try:
                products[choose].list() 
                
            except TypeError:
                print ("Please enter valid choose")
                return ui(x,age,option,user)
        except ValueError:
            print ("please enter a valid \033[1m   NUMBER \033[0m")
            return ui(x,age,option,user)
    elif option.lower() == "buy":
        pass
    elif option.lower() == "remove from cart":
        pass
    elif option.lower() == "checkout":
        pass
    else:
        print ("Please enter valid option")
        return options(x,age)
    







def options(x,age,user):
    # Allows the user to choose
    print ('''\033[1mEnter:\033[0m
        \033[1m   Account \033[0m
           Details - TO display account details
        \033[1m   Bank \033[0m
           Deposit - To deposit money into bank account
           Withdraw - To withdraw money from bank account
           Display - To display details of your bank account
        \033[1m   Shopping \033[0m
           Products - To list all products available
           Purchase - To add an available item to the cart 
           Remove - To remove item from cart
           Checkout - To purchase items
           ''')
    option = input("What do you want to do, " + x.title() + " " )
    ui (x,age,option,user)
    





def logon(x):
    #validation for failing attempts
    global lockingout
    if lockingout == 3:
        print ("Failed too many times. You have been locked out.")
        quit()
    else:
        if x.lower() == "aidan":
            print ("Welcome, Aidan")
            age = -127
            user = Bank(x,age)
            options(x,age,user)
        elif x.lower() == "akhil":
            print ("Welcome, Akhil")
            age = 17
            user = Bank(x,age)
            options(x,age,user)
        elif x.lower() == "adam":
            print ("Welcome, Adam")
            age = 1
            user = Bank(x,age)
            options(x,age,user)
            
            
        else:
            print ("You have failed to enter a valid user")
            lockingout = lockingout + 1
            return logon(input ("please enter a name "))
lockingout = 0
startuser = input ("Please enter a name ")
logon(startuser)

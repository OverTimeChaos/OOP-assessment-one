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
        print (f"New balance is ${self.balance}")
    def withdraw (self,amount):
        #allows user to redraw money from account
        self.balance = self.balance - amount
        print (f"New balance is ${self.balance}")
    def displaybank (self):
        # display balance
        print ("Balance: $" + str(self.balance))
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
    def reduce(self):
        #Reduces the amount of that product
        self.quantity = self.quantity - 1
    def increase(self):
          #increases the amount of that product
        self.quantity = self.quantity + 1
class Cart(Product):
    def __init__ (self):
        self.cart = [0,0,0,0]
    def add (self,choose):
        if choose == 'computer':
            self.cart[0] += 1
        elif choose == 'laptop':
            self.cart[1] += 1
        elif choose == 'mouse': 
            self.cart[2] += 1
        elif choose == 'keyboard':
            self.cart[3] += 1
    def remove (self,choose):
        if choose == 'computer':
            self.cart[0] -= 1
        elif choose == 'laptop':
            self.cart[1] -= 1
        elif choose == 'mouse': 
            self.cart[2] -= 1
        elif choose == 'keyboard':
            self.cart[3] -= 1
    def show(self,number):
        # shows the amount of the item in cart
        return self.cart[number]
    def showar(self):
        # shows the amount of things in the cart
        return self.cart





        
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
            print ("please enter a valid \033[1mNUMBER\033[0m")
            return ui(x,age,option,user)
    elif option.lower() == "display":
        # displays user's bank details
        user.displaybank()
        return options(x,age,user)
    elif option.lower() == "products":
        #Displays a list of available products 
        print ('''\033[1mAvailable products:\033[0m  
               1 - Computer
               2 - Laptop
               3 - Mouse
               4 - Keyboard''')
        try:
            choose = int (input("Input a valid number "))-1
            try:
                products[choose].list() 
                return options(x,age,user) 
                
            except TypeError:
                print ("Please enter valid choose")
                return ui(x,age,option,user)
        except ValueError:
            print ("please enter a valid \033[1mNUMBER\033[0m")
            return ui(x,age,option,user)
    elif option.lower() =="current":
        #display's current items in cart
        print (f'''Current items in cart:
Computer - {cart.show(0)}
Laptop - {cart.show(1)}
Mouse - {cart.show(2)}
Keyboard - {cart.show(3)} ''')
        options(x,age,user)    
    elif option.lower() == "purchase":
        print ('''               1 - Computer
               2 - Laptop
               3 - Mouse
               4 - Keyboard''')
        try:
            choose = int (input("Input a valid number "))-1
            try:
                #checks if there is that product exists in the cart 
                if products[choose].quantity == 0:
                    print ("Sorry there is none left of that product" )
                    return options(x,age,user) 
                else:
                    products[choose].reduce()
                    print ("Adding product")
                    cart.add(productstr[choose])
                    return options(x,age,user) 
            except IndexError:
                print ("Please enter valid choose")
                return ui(x,age,option,user)
        except ValueError:
            print ("please enter a valid \033[1mNUMBER\033[0m")
            return ui(x,age,option,user)
    elif option.lower() == "remove":
        print ('''               1 - Computer
               2 - Laptop
               3 - Mouse
               4 - Keyboard''')
        try:
            choose = int (input("Input a valid number "))-1
            try:
                #checks if there is that product left
                if cart.show(choose) == 0:
                    print ("Sorry there is none left of that product in the cart" )
                    return options(x,age,user) 
                else:
                    products[choose].increase()
                    print ("Removing")
                    cart.remove(productstr[choose])
                    return options(x,age,user) 
            except IndexError:
                print ("Please enter valid choose")
                return ui(x,age,option,user)
        except ValueError:
            print ("please enter a valid \033[1mNUMBER\033[0m")
            return ui(x,age,option,user)
    elif option.lower() == "checkout":
         #allows people to check out
         print (f'''Current items in cart:
Computer - {cart.show(0)} - ${cart.show(0)*computer.price}
Laptop - {cart.show(1)} - ${cart.show(1)*laptop.price}
Mouse - {cart.show(2)} - ${cart.show(2)*mouse.price}
Keyboard - {cart.show(3)} - ${cart.show(3)*keyboard.price} ''')
         input ('Press enter to continue ')
         total = cart.show(0)*computer.price + cart.show(1)*laptop.price + cart.show(2)*mouse.price + cart.show(3)*keyboard.price
         if total > user.balance:
            print ("Not enough funds in bank account to purchase items. Please remove some items")
            return options(x,age,user)
         elif list(cart.showar()) == [0] * len(cart.showar()):
             print ("There is no items in the cart")
             return options(x,age,user)
         else:
             print ("Checking out...")
             user.withdraw(total)
             print ("Checked out. Thank you for purchase at [redacted]")
             quit()
            

                 
    else:
        print ("Please enter valid option")
        return options(x,age,user)
    


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
           Current - To check current items in cart
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
computer = Product("Computer","A personal electronic device",15,500)
laptop = Product("Laptop","A portable personal electronic device",5,600)
mouse = Product ("Mouse","A device that allows manipulation of the cursor",50,50)
keyboard = Product ("Keyboard","A device that allows you to type with your device",50,50)
products = [computer,laptop,mouse,keyboard]
productstr = ["computer","laptop","mouse","keyboard"]
cart = Cart()
lockingout = 0
startuser = input ("Please enter a name ")
logon(startuser)

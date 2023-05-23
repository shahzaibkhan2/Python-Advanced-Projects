# 1. FIRST CLASS TO MAKE.

class Atm: # class
    
    __counter = 1  # STATIC VARIABLE
    
    # Constructor for Class
    def __init__(self):  
        self.__pin = ''     # __ MEANS THIS VARIABLE INSTANCE IS HIDDEN AND NOT VISIBLE TO PUBLIC. 
        self.__balance = 0
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter + 1 # TODO SHAHZAIB KHAN'S WORK     
        self.menu()
    
    # Static method    
    @staticmethod
    def get_counter():  # YOU CAN AVOID SELF IN STATIC METHOD. THEY GENERALLY DONT USE SELF ARGUMENT.    
        return Atm.__counter
        
     
    # A function to get balance   
    def get_balance(self):   # THIS IS GETTER METHOD TO PROTECT INSTANCE VARIABLES, IN CASE WHEN SOMEONE GETS MEMORY ADDRESS OF INSTANCE VARIABLE. 
        return self.__balance
    
    # A function to set balance 
    def set_balance(self,new_value):   # THIS IS A SETTER METHOD TO PROTECT INSTANCE VARIABLES, IN CASE WHEN SOMEONE GETS MEMORY ADDRESS OF INSTANCE VARIABLE.
        
        if type(new_value) == int:
            self.__balance = new_value
                
        else:
            print('sorry invalid command. enter a valid amount in digits.')
        
        
    # A function to create menu for the user    
    def menu(self): 
        user_input = input("""Hi how may i help you?\n 
        1. Press 1 to create pin 
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit\n""")

    
        if user_input == '1':
            self.create_pin()
        # create pin
        
        elif user_input == '2':
            self.change_pin()
        # change pin
        
        elif user_input == '3':
            self.check_balance()
        # check balance
        
        elif user_input == '4':
            self.withdraw()
        # withdraw
        
        elif user_input == '5':
            print('thank you very much for using our bank services!. have a good day!')
            exit()
            
    # A function to create pin   
    def create_pin(self): 
        user_pin = input('enter your pin please !\n')
        self.__pin = user_pin
        
        user_balance = int(input('enter your balance please !\n'))
        self.__balance = user_balance
        
        print('pin created successfully.')
        self.menu()
    # A function to change pin
    def change_pin(self): #function
        old_pin = input('enter your old pin! \n')
        
        if old_pin == self.__pin :
            
            new_pin = input('enter new pin: \n')
            self.__pin = new_pin
            print('pin changed successfully!')
            self.menu()

        else:
            print('incorrect pin.')
            self.menu()
    # A function to check balance        
    def check_balance(self): #functon
        user_pin_check = input('enter your pin:  ')
        if user_pin_check == self.__pin:
            print('your balance is: ',self.__balance)
            self.menu()
            
        else:
            print('incorrect pin please try again!')
            self.menu()
    # A function to withdraw balance        
    def withdraw(self):
        user_withdraw_pin = input('enter your pin: ')
        if user_withdraw_pin == self.__pin:
            amount = int(input('enter your amount: '))
            if amount <= self.balance:
                self.__balance = self.__balance - amount
                print('withdraw is successful! . your current balance is: ',self.__balance)
            
            else:
                print('sorry ! you have insuficient balance to complete withdraw.')
        else:
            print('incorrect pin . please try again! ')

        self.menu()

# Object and input area    
obj = Atm()


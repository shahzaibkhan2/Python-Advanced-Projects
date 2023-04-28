from cProfile import label
from glob import glob
import os
from sqlite3 import register_adapter
from tkinter import *
from PIL import ImageTk,Image

# Main Screen

master = Tk()
master.title('Banking app')
master.geometry("200x400")

# functions

def finish_reg():
    
    name= temp_name.get()
    age= temp_age.get()
    gender= temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    
    
    if name=="" or age =="" or gender=="" or password=="":
        notif.config(fg="red",text="All fields are required !!")
        return
    for name_check in all_accounts:
        if name== name_check:
            notif.config(fg="red",text="This account already exits.")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+"\n")
            new_file.write(gender+"\n")
            new_file.write(age+"\n")
            new_file.write(password+"\n")
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="congratulations!! your account has been created successfully.")


def register():
    # Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    
    temp_name= StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    
    register_screen = Toplevel(master)
    register_screen.title("Register")
    
# Labels
    Label(register_screen,text="Please enter the details below to fill the form",font=("Time New Roman",10,"bold")).grid(row=0,sticky=N,pady=10)
    Label(register_screen,text="Name",font=("Time New Roman",10)).grid(row=1,sticky=W)
    Label(register_screen,text="Age",font=("Time New Roman",10)).grid(row=2,sticky=W)
    Label(register_screen,text="Gender",font=("Time New Roman",10)).grid(row=3,sticky=W)
    Label(register_screen,text="Password",font=("Time New Roman",10)).grid(row=4,sticky=W)
    
    # entries
    
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)
    notif = Label(register_screen,font=("Time New Roman",10))
    notif.grid(row=6,sticky=N,pady=10)
    
    # button
    
    Button(register_screen,text="Register",command=finish_reg,font=("Time New Roman",10,"bold")).grid(row=5,sticky=N,pady=10)
    
    
    #login functions
    
def login_session():
    # globals
    global login_name
    
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    all_accounts = os.listdir()
    for name in all_accounts:
        if name==login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[3]
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                
                # labels
                Label(account_dashboard,text="Personal Account Details",font=("Time New Roman",12,"bold")).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard,text="Welcome, "+ name,font=("Time New Roman",12,"bold")).grid(row=1,sticky=N,pady=10)
                # buttons
                Button(account_dashboard,text="Personal Details",font=("Time New Roman",10),width=30,command=personal_details).grid(row=2,sticky=N,padx=5)
                Button(account_dashboard,text="Deposit",font=("Time New Roman",10),width=30,command=deposit).grid(row=3,sticky=N,padx=5,pady=5)
                Button(account_dashboard,text="Withdraw",font=("Time New Roman",10),width=30,command=withdraw).grid(row=4,sticky=N,padx=5,pady=5)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                
                
                
                
            return
        else:
            login_notif.config(fg="red",text="Incorrect password !")
    login_notif.config(fg="red",text="No such account found !")
    
def deposit():
    # Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount= StringVar()
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    
    # labels
    
    Label(deposit_screen,text="Deposit",font=("Time New Roman",10,"bold")).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen,text="Current balance : Rs."+details_balance,font=("Time New Roman",9))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen,text="Amount : Rs.",font=("Time New Roman",9)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen,font=("Time New Roman",10))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    
    # entries
    Entry(deposit_screen,textvariable=amount).grid(row=2,column=1)
    # button
    Button(deposit_screen,text="Finish",font=("Time New Roman",10,"bold"),command=finish_deposit).grid(row=3,sticky=W,pady=5)
    
def finish_deposit():
    if amount.get()=="":
        deposit_notif.config(text="Amount is required !",fg="red")
        return
    if float(amount.get())<=0:
        deposit_notif.config(text="Negative Currency is not accepted !",fg="red")
        return
    file = open(login_name,'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance)+ float(amount.get())  
    file_data = file_data.replace(current_balance,str(updated_balance))  

    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.config(text="Current balance Rs. "+str(updated_balance),fg="green")
    deposit_notif.config(text="Balance updated successfully !",fg="green")

    

    
    

def withdraw():
    
     # Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount= StringVar()
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    # withdraw screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")
    
    # labels
    
    Label(withdraw_screen,text="Withdraw",font=("Time New Roman",10,"bold")).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen,text="Current balance : Rs."+details_balance,font=("Time New Roman",9))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen,text="Amount : Rs.",font=("Time New Roman",9)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_screen,font=("Time New Roman",10))
    withdraw_notif.grid(row=4,sticky=N,pady=5)
    
    # entries
    Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1)
    # button
    Button(withdraw_screen,text="Finish",font=("Time New Roman",10,"bold"),command=finish_withdraw).grid(row=3,sticky=W,pady=5)
    
def finish_withdraw():
    if withdraw_amount.get()=="":
        withdraw_notif.config(text="Amount is required !",fg="red")
        return
    if float(withdraw_amount.get())<=0:
        withdraw_notif.config(text="Negative Currency is not accepted !",fg="red")
        return
    file = open(login_name,'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = (details[4])
    
    if float(withdraw_amount.get())>float(current_balance):
        withdraw_notif.config(text="Insufficient funds !",fg="red")
        return
        
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())  
    file_data = (file_data.replace(current_balance,str(updated_balance))) 

    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.config(text="Current balance Rs. "+str(updated_balance),fg="green")
    withdraw_notif.config(text="Balance updated successfully !",fg="green")
    
        
    
   
   

def personal_details():
    # Vars
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    detail_name = user_details[0]
    detail_gender= user_details[1]
    detail_age = user_details[2]
    detail_balance = user_details[4]
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal details")
    
    # labels
    Label(personal_details_screen,text="Personal Details",font=("Time New Roman",11,"bold")).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen,text="Name : " + detail_name,font=("Time New Roman",9)).grid(row=1,sticky=W)
    Label(personal_details_screen,text="Gender : " + detail_gender,font=("Time New Roman",9)).grid(row=2,sticky=W)
    Label(personal_details_screen,text="Age : " + detail_age,font=("Time New Roman",9)).grid(row=3,sticky=W)
    Label(personal_details_screen,text="Balance Rs.: " + detail_balance,font=("Time New Roman",9)).grid(row=4,sticky=W)
        
def login():
    # Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    
    
    login_screen = Toplevel(master)
    login_screen.title("Login") 

    # Labels
    Label(login_screen,text="Login to your account ",font=("Time New Roman",12,"bold")).grid(row=0,sticky=N,pady=10)
    Label(login_screen,text="User Name ",font=("Time New Roman",8,"bold")).grid(row=1,sticky=W)
    Label(login_screen,text=" Password ",font=("Time New Roman",8,"bold")).grid(row=2,sticky=W)
    login_notif=Label(login_screen,font=("Time New Roman",10))
    login_notif.grid(row=4,sticky=N)
    
    # entries
    
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)
    
    # button
    Button(login_screen,text="Login",width=15,command=login_session,font=("Time New Roman",10,"bold")).grid(row=3,sticky=N,padx=5,pady=5)

# Importing images

img = Image.open("banking.png")
img = img.resize((160,160))
img = ImageTk.PhotoImage(img)

# labels

Label(master, text="Khan Banking App",font=("Time New Roman",15)).grid(row=0,sticky=N)
Label(master, text="Trusted and most reliable",font=("Time New Roman",10)).grid(row=0,sticky=N,pady=30)
Label(master, image=img).grid(row=1,sticky=N,pady=15)

# Buttons

Button(master,text="Register",font=("Time New Roman",10,"bold"),width=15,command=register).grid(row=3,sticky=N,pady=9)
Button(master,text="Login",font=("Time New Roman",10,"bold"),width=15,command=login).grid(row=4,sticky=N,pady=9)




master.mainloop()

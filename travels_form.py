from tkinter import *

root = Tk()
root.geometry("644x344")
root.title("SS Travels")
def get_form():
    print("Submitting form...")
    
    with open("form.txt","a") as f:
        f.write(f"{name_value.get(),phone_value.get(),gender_value.get(),emergency_value.get(),payment_value.get(),food_service_value.get()}\n")
       
    
    
    
        

Label(root,text="Welcome to SS travels",font="cosmicsansms 13 bold").grid(row=0,column=2,pady=15)

name = Label(root,text="Name")
phone = Label(root,text="Phone Number")
gender = Label(root,text="Gender")
emergency = Label(root,text="Emergency Contact")
payment = Label(root,text="Payment Method")

name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
payment.grid(row=5,column=1)

# -----------------------------------------------------------------------------------------------------------------

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_value = StringVar()
food_service_value = IntVar()

name_entry = Entry(root,textvariable=name_value)
phone_entry = Entry(root,textvariable=phone_value)
gender_entry = Entry(root,textvariable=gender_value)
emergency_entry = Entry(root,textvariable=emergency_value)
payment_entry = Entry(root,textvariable=payment_value)

name_entry.grid(row=1,column=2)
phone_entry.grid(row=2,column=2)
gender_entry.grid(row=3,column=2)
emergency_entry.grid(row=4,column=2)
payment_entry.grid(row=5,column=2)

# ---------------------------------------------------------------------------------------------------------------------
check_but_food_ser = Checkbutton(text="Do you want to prebook your meals?",variable=food_service_value)
check_but_food_ser.grid(row=6,column=2)

button_food_ser = Button(text="Submit Now",command=get_form).grid(row=7,column=2)









mainloop()
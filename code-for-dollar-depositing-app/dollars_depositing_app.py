from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x300")
root.title("Menu Practice")

def get_dollar():
    print(tmsg.showinfo("Transaction",f"{my_slider.get()}$ have been deposited to your account"))

def get_help():
    tmsg.askquestion("How was your experience?","tell us what is your problem by saying yes or no!")
    
def rate_us():
    value = tmsg.askquestion("How was your experience ?","Please let us know by clicking Yes or No!")
    if value=="yes":
        print("Thank you very much for your feedback!")
    else:
        print("We are collecting information about your problem and will get back to you soon!")
    
    
main_menu = Menu(root)

m1 = Menu(main_menu,tearoff=0)
m1.add_command(label="Save")
m1.add_command(label="Save As")
m1.add_separator()
m1.add_command(label="New Project")
main_menu.add_cascade(label="Files",menu=m1)
root.config(menu=main_menu)

m2 = Menu(main_menu,tearoff=0)
m2.add_command(label="Copy")
m2.add_command(label="Paste")
m2.add_separator()
m2.add_command(label="Cut")
m2.add_command(label="Paste")
main_menu.add_cascade(label="Edit",menu=m2)
root.config(menu=main_menu)

m3 = Menu(main_menu,tearoff=0)
m3.add_command(label="Help",command=get_help)
m3.add_command(label="Rate Us",command=rate_us)
main_menu.add_cascade(label="Help",menu=m3)
root.config(menu=main_menu)


# this is packing and buttons of the slider section
Label(root,text="How many dollars you want to deposit?").pack()
my_slider = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)   # tickinterval gives the checkpoints of values by which a user can easily get to that desired value.
my_slider.set(10)  # this set function sets the default value as 10 but you can also scroll your slider to 0.
my_slider.pack()

Button(root,text="Get Dollars!!",pady=10,font="bold",command=get_dollar).pack()













mainloop()
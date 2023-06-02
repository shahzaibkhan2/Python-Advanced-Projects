from distutils.cmd import Command
from imaplib import Commands
from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")  
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /r /t 1")    
    
st = Tk()
st.title("Shutdown App")
st.geometry("600x600")
st.config(bg="Blue")
restart_button = Button(st,text="Restart", font=("Time New Roman",30,"bold"),relief=RAISED,cursor="Plus",command=restart)
restart_button.place(x=150,y=60,height=60,width=200)

restart_time = Button(st,text="Restart Time", font=("Time New Roman",30,"bold"),relief=RAISED,cursor="Plus",command=restart_time)
restart_time.place(x=150,y=130,height=60,width=260)

logout_button = Button(st,text="Logout", font=("Time New Roman",30,"bold"),relief=RAISED,cursor="Plus",command=logout)
logout_button.place(x=150,y=200,height=60,width=200)

shutdown_button = Button(st,text="Shutdown", font=("Time New Roman",30,"bold"),relief=RAISED,cursor="Plus",command=shutdown)
shutdown_button.place(x=150,y=270,height=60,width=200)








st.mainloop()
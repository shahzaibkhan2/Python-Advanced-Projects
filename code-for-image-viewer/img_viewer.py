from glob import glob
from tkinter import *
from PIL import ImageTk,Image
import os

def next_func():
    global counter
    img_label.config(image=files_array[counter%len(files_array)])
    counter = counter+1

counter = 1
root = Tk()
root.title("Image Viewer")
root.geometry("350x500")
root.configure(background="black")
       

files = os.listdir('new2icons')
files_array = []
for file in files:
    img = Image.open(os.path.join('new2icons',file))
    
    img_resize = img.resize((200,300))
    files_array.append(ImageTk.PhotoImage(img_resize))
    
img_label = Label(image=files_array[0])
img_label.pack(pady=5)

next_btn = Button(root,text="Next",bg="white",fg="black",font=("verdana",10,"bold"),width=25,height=2,command=next_func)
next_btn.pack(pady=5)
    
    








root.mainloop()
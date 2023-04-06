from tkinter import *
import speedtest

def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download()/(10**6),3))+"Mbps"
    up = str(round(st.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

st = Tk()
st.title("Internet Speed Test")
st.geometry("500x650")
st.config(bg="light blue")
lab = Label(st,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="light blue",fg="gray")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(st,text="download Speed",font=("Time New Roman",25,"bold"))
lab.place(x=60,y=140,height=50,width=380)

lab_down = Label(st,text="00",font=("Time New Roman",25,"bold"))
lab_down.place(x=60,y=240,height=50,width=380)

lab = Label(st,text="Upload Speed",font=("Time New Roman",25,"bold"))
lab.place(x=60,y=340,height=50,width=380)

lab_up = Label(st,text="00",font=("Time New Roman",25,"bold"))
lab_up.place(x=60,y=440,height=50,width=380)

button = Button(st,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",bg="sky blue",command=speedcheck)
button.place(x=60,y=540,height=50,width=380)


st.mainloop()
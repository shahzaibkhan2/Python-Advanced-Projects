# Work To Do
from time import *
import random as r
def mistake(partest,usertest): 
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except:
            error = error+1
    return error

def time_speed(time_s,time_e,user_input):
    time_delay = time_e - time_s
    time_R= round(time_delay,2)
    speed = len(user_input)/time_R
    return round(speed)
if __name__=='__main__':
    while True:
        ck = input("are you ready to type? yes/no: ")
        if ck=="yes":

            test= ["RAM stands for random access memmory and it's work is to store temporary data in computer","welcome to the python and let's learn it with ease","computer programming is a very dynamic language and is used in all machines"]
            test1 = r.choice(test)
            print("    ***** typing speed *****")
            print(test1)
            print()
            print()
            time1 = time()
            user_input = input("start typing : ")
            time2 = time()

            print("speed: ",time_speed(time1,time2,user_input),"w/sec")
            print("errors: ", mistake(test1, user_input))
            
        elif ck == "no":
            print("thank you and have a good day!")
            break
        else:
            print("wrong answer please give a valid answer.")
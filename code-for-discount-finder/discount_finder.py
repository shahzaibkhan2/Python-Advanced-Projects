# 1. IF ELSE LADDER
pur_amount = int(input("Enter your amount: Rs."))
if pur_amount<10000:
    print("10% Discount")
else:
    if pur_amount>10000 and pur_amount<20000:
        print("20% Discount")
    else:
        if pur_amount > 20000 and pur_amount<30000:
            print("30% Discount")
            
        else:
            if pur_amount > 30000:
                print("40% Discount")


# 2.YOU CAN DO THE SAME WITH ELIF(ELSE IF) TO SOLVE THIS PROBLEM
pur_amount = int(input("Enter your amount: Rs."))
if pur_amount<10000:
    print("10% Discount")
elif pur_amount>10000 and pur_amount<20000:
    print("20% Discount")
elif pur_amount > 20000 and pur_amount<30000:
    print("30% Discount")
else:
    print("40% Discount")
print("thank you for shopping with Khan group")



    
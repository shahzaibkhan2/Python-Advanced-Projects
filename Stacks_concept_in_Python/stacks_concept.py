listt = []

while True:

    try:

        option = int(input("""    1 to Enter element
        2 to Pop element
        3 to find Peek
        4 to Display Stack
        5 to Exit: \n"""))

        if option == 1:
            quantity_to_store = int(input("Enter quantity to store: "))
            listt.append(quantity_to_store)
            print("This is list -----> ", listt)

        elif option == 2:
            if listt == 0:
                print("Sorry Empty List")
            else:
                n = listt.pop()
                print("Removed Element ----> ", n)

        elif option == 3:
            if listt == 0:
                print("Sorry Empty List")
            else:
                p = listt[-1]
                print("This is Peek Value ----> ", p)
        elif option == 4:
            print("This is Stack ----> ", listt)

        elif option == 5:
            break

        else:
            print("Invalid Choice")
    
    except Exception as e:
        print("Please enter a valid number not a string / alphabet. ")
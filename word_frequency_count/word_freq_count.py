def freq(string):
    """ A function to find maximum frequency of the word occurring in the string 
    Input: Give it a string
    Output: Word : with max frequency in digits"""
    d = {}
    
    for i in string.split():
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
            
    max_value = max(d.values())
    
    for i in d:
        if d[i] == max_value:
            print(i, "--> ", d[i])
            break
    
freq('hello hello hello hello hello hello hello hello hello you i am fine thank you')
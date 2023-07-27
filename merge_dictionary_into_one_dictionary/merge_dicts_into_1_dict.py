def dict_convert(*kwargs):
    """ A function to merge any number of dictionaries into one dictionary 
    input: Give it any number of Dictionaries
    Output: A single dictionary"""
    d = {}
    for i in kwargs:
        d.update(i)
    return d


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict_convert(dic1, dic2, dic3)
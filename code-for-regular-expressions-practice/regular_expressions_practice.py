import re

temp_string = "Shahzaib got 99 marks and Yasir got 100 marks"

match = re.findall(r"[A-Z][a-z]*", temp_string)
print(match)

w = re.compile("[a-t]")
match = re.findall(w,temp_string)
print(match)

p = re.split("\d+",temp_string)
print(p)

p1 = re.sub("\s+", "",temp_string)
print(p)

p2 = re.escape(temp_string)
print(p)

# Prints only first value, not all values as findall() does
p3 = re.search(r"\d+",temp_string)
print(p)

phone = "(092)-(309)-(3343432) 999 333 222 34343 t444"

pattern = re.findall("\(\d{3}\)-\(\d{3}\)-\(\d{7}\)",phone)
print(pattern)

email = "shahzaib%32@gmail.com shahzaib4444@gmail.com shahzaib@gmail.com dr.com"

pattern = re.findall("[\w._%]{0,20}@[\w].[\w]{2,3}",email)
print(pattern)

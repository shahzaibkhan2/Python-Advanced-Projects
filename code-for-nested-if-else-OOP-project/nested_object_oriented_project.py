# 1. INHERITANCE EXAMPLE
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Cat(Pet):
    def speak(self):
        print('mew mew')

    
    
class Dog(Pet):
    
    def speak(self):
        print('bark bark')

    
c = Cat('bill', 44)
d = Dog('tim', 33)
print(c.name)
print(c.age)
print(d.name,d.age)
print(d.speak())

# 2. CLASS ATTRIBUTE EXAMPLE

class Person:
    number_of_people = 0   # this class attribute is used for constant values like gravity which have -9.8 . in this way this value will be same through out the class
    
    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1  # look at this ! you can also increment your class attribute values

p1 = Person('bill')
p2 = Person('tim')
print(Person.number_of_people)

class Person:
    number_of_people = 0   # this class attribute is used for constant values like gravity which have -9.8 . in this way this value will be same through out the class
    
    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod   # its a class method which means it only binds with a class and remains in class
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
    @staticmethod   # static method means no argument to pass and stays bound to class and remains same
    def add5(x):
        return x + 5
    

p1 = Person('tim')
p2 = Person('bill')
print(p1.number_of_people_())
print(Person.add5(10))


class Employee:
    increment = 1.3
    number_of_employee = 0
    
    def __init__(self,name,age,gender,salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        Employee.number_of_employee += 1
        
    def increase_salary(self):
        self.salary = int(self.salary * Employee.increment)
    
    @classmethod
    def increase_increment(cls,amount):  # class method takes the class itself as an argument which is cls here
        cls.increment = amount
        
    @classmethod
    def with_str(cls,emp_string):
        name,age,gender,salary = emp_string.split('-')
        return cls(name,age,gender,salary)
    
    @staticmethod
    def is_open(day):
        if day == 'sunday' or day == 'saturday':
            return 'office is closed'
        else:
            return 'office is open'
        
        
class Programmer(Employee):
    
    def __init__(self, name, age, gender, salary,prolang,exp):
        super().__init__(name, age, gender, salary)
        self.prolang = prolang
        self.exp = exp
        
    def __add__(self,other):    # this is a dunder method or magic method which adds the salaries of two objects shahzaib and yasir
        return self.salary + other.salary
        
        
    def increase_salary(self):
        self.salary = int((self.salary * Employee.increment) * 1)
        
    def __repr__(self):  # you can also use many magic methods like string and add etc. to make code more readable
        return 'Employee ({} , {} , {} , {} , {} , {} )'.format(self.name,self.age,self.gender,self.salary,self.prolang,self.exp)
        
    
        
        
        
# private = Employee.with_str('shah zaib-25-male-2500000')
# print(private.is_open('friday'))    # you can also use object to call is_open function
# print(Employee.is_open('sunday'))   # you can call is_open function using class
# print(private.name,private.age,private.gender,private.salary)
shahzaib = Programmer('shahzaib', 25, 'male', 2400000,'Python',15)
print(Programmer.__repr__(shahzaib))
# shahzaib.increase_salary()
# print(shahzaib.salary)
# yasir = Employee('yasir', 21, 'male', 2400000)
# print(Programmer.__add__(shahzaib, yasir))
# Employee.increase_increment(2)
# shahzaib.increase_salary()
# print(shahzaib.salary)
# yasir.increase_salary()
# print(yasir.salary)
# print(Employee.number_of_employee)
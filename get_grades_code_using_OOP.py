class Student:
    
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
        
class Course:
    
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_students(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grades(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
        return value / len(self.students)
    
s1 = Student('shahzaib', 25, 99)
s2 = Student('yasir', 20, 98)
s3 = Student('shoib', 7, 89)

course = Course('science', 2)
print(course.add_students(s1))
print(course.add_students(s2))
print(course.students[1].name)
print(course.get_average_grades())


        
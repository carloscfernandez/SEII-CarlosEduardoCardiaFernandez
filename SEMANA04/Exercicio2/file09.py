class Student:
    def __init__(self,name,age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]
        self.is_active=False
    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
    return False
    def get_avarege_grade(self):
        value=0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.student)

s1=Student("Tim",19,95)
s2=Student("Bill",19,75)
s3=Student("Jim",19,65)

course=Sourse("Science",2)
course.add_student(s1)
course.add_student(s2)
print(course.get_avarege_grade())
print(course.student(s3))
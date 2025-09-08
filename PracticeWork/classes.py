# oops Examples
'''
class Student:
    def read():
        print("Student can read")
    def write():
        print("Student can write")

class Teacher(Student):
    def teach():
        print("Teacher can teach")

obj = Student
obj.read()
obj.write()

t = Teacher
t.read()
t.write()
t.teach()

'''

class Mobile:
    def __init__(self,camera,RAM):
        self.cam = camera
        self.ram = RAM
        print(f"Mobile features has {self.cam} camera and {self.ram} RAM")

oppo = Mobile("50mp","64GB")
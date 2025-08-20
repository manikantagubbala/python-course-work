'''
print("Book Details Display")

class Book:
    def __init__(self):
        self.title = title
        self.author = author
        self.price = price

        print(f"\nBook Name: {self.title} \nName of the Book Author: {self.author} \nPrice: Rs.{self.price}")


title = input("Enter Book title: ")  
author = input("Enter Boook Author: ")
price = int(input("Enter Book Price: "))

obj = Book()


# Another Way

class Books:
    def __init__(self,title, author, year):
        self.title = title
        self.author = author 
        self.year = year

    def display(self):
        print(f"\nBook Name: {self.title} \nName of the Author: {self.author} \nBook Price: {self.year}")

title = input("Enter Title: ")
author = input("Enter Author: ")
year = int(input("Enter Invented Year: "))

obj = Books(title, author, year)
obj.display()

'''

'''
print("Employee Salry Calculator")

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_annual_salary(self):
        return self.base_salary * 12
    
obj = Employee("Manikanta", 35000)
print("Annual Salary: ",obj.calculate_annual_salary())

'''

'''
print("Student Grade Evaluator")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if sum(self.marks) / len(self.marks) >= 40:
            return "Pass"
        else:
            return "Fail"
        
obj = Student("Manikanta", [55,67,69])
print("Result: ", obj.result())

'''


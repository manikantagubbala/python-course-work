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

# Encapsulation
# public
class Hotel:
    def __init__(self, name):
        self.name = name
    
obj = Hotel("Biryani")
print(f"{obj.name} is an item of Bawarchi")

obj.name = "Chicken Biryani"
print(f"\nAfter Modifying \n{obj.name} is an item of Bawarchi")

# private
class Resaturant:
    def __init__(self, price):
        self.__price = price
    
    def getprice(self):
        return self.__price

    # modify
    def updateprice(self, newprice):
        self.__price = newprice

hababi = Resaturant(199)
print(f"\n(Private method) Biryani Price : ₹.{hababi.getprice()}")

hababi.updateprice(149)
print(f"\nAfter Modifying \nBiryani Price : ₹.{hababi.getprice()}")


# protected
class Tiffin:
    @property
    def kitchen(self):
        self._item = item
        return self._item
    
    # modify
    @kitchen.setter
    def kitchens(self):
        self._item = newitem

item = "Dosa"    
taza = Tiffin()
print(f"\n(Protected) {taza.kitchen} is an item of Taza Kitchen")

newitem = "Karamdosa"
print(f"\nAfter Modifying \n{taza.kitchens} is an item of Taza Kitchen")
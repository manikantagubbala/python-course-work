# GrandTest.py

'''

n = 30
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print(f"{n} is not a Prime Number")
            break
    else:
        print("{n} is a Prime Number")
else:
    print("It is Not a Prime Number")



num = int(input("Enter the Number: "))
count = []
for i in range(2,num):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        count.append(i)
print(len(count))


# Patterns
n = 5
print("Pattern - 1")
for row in range(n):
    for col in range(row + 1):
        print(col, end =" ")
    print()


print("\nPattern - 2")
for row in range(1,n):
    for col in range(1,n):
        print(row, end = " ")
    print()

print("\nRightAngleTriangle - Pattern - 3")
for row in range(1, n):
    for col in range(row):
        print("*", end=" ")
    print()

print("\nPattern - 4")
for row in range(1,n):
    for col in range(n-row):
        print(" ", end=" ")
    for i in range(2*row - 1):
        print("*", end=" ")
    print()

print("\nPattern - 5")
for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

#n=8
#print("\nPattern - 6")
#for row in range(1, n):
#    if row < n//2:
#        for col in range(n - row):
#            print("-", end=" ")
#        for i in range(2*row - 1):
#            print("*", end=" ")
#        print()
#    elif row > n//2:
#        for col in range(row - n//2+1):
#            print("-", end=" ")
#        for i in range(2*(n - row)+1):
#            print("*", end=" ")
#        print()    

'''
'''
n = int(input("Enter number of rows (odd number): "))

mid = n // 2 + 1   # middle row

for row in range(1, n+1):
    if row <= mid:  # upper part (including middle)
        # spaces
        for col in range(mid - row):
            print(" ", end=" ")
        # stars
        for i in range(2*row - 1):
            print("*", end=" ")
    else:           # lower part
        # spaces
        for col in range(row - mid):
            print(" ", end=" ")
        # stars
        for i in range(2*(n - row) + 1):
            print("*", end=" ")
    print()

'''
'''

print("\nPattern - 6")
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0:
            print("*", end=" ")
    print()

print("\nPattern - 7")
for row in range(n):
    print("*", end=" ")

print("\nPattern - 8")
for col in range(n):
    print("*")

print("\nPattern - 9")
for row in range(n):
    for col in range(n):
        if row == n-1 or col == n-1 or row == 0 or col == 0 or col == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("\nOne - Pattern - 10")
for row in range(n):
    for col in range(n):
        if row == n-1 or col == n//2 or (row <= n//2 and (row+col == n//2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nTriangle - Pattern - 11")
for row in range(n):
    for col in range(2*n -1):
        if row == n-1 or (col<=n-1 and row+col == n-1) or (col >= n and col-row == n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("\nPattern - 12")
for row in range(n):
    for col in range(n):
        if (row+col) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

print("\nInverted right-angled triangle - Pattern - 13")
for row in range(n):
    for col in range(n - row):
        print("*", end=" ")
    print()


print("\nReverse Pyramid - Pattern - 14")
for row in range(n):
    for spa in range(row):
        print(" ", end="")
    for col in range(n - row):
        print("*", end=" ")
    print()


print("\nPyramid - Pattern - 15")
for row in range(n+1):
    for spa in range(n - row):
        print(" ", end="")
    for col in range(row):
        print("* ", end="")
    print() 


print("\nFloyd’s Triangle - Pattern - 16")
nums = 1
for row in range(n):
    for num in range(row + 1):
        print(nums, end=" ")
        nums += 1
    print()

print("\nPascal’s Triangle - Pattern - 17")
for row in range(n+1):
    for spa in range(n - row):
        print(" ", end="")
    number = 1
    for num in range(row + 1):
        print(f'{number} ', end="")
        number = number * (row - num) // (num + 1)
    print()


print("\nInverted number - Pattern - 18")
for row in range(1,n):
    for col in range(1, n - row + 1):
        print(col, end=" ")
    print()


Diamond pattern:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

Hourglass pattern:
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *

Palindromic number triangle:
    1
   121
  12321
 1234321
123454321

Butterfly pattern:
*       *
* *   * *
* * * * *
* *   * *
*       *

Checkerboard pattern:
* * * * 
 * * * *
* * * *
 * * * *

'''

'''
class Student:
    totalStudents = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.totalStudents += 1
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def get_total_students(cls):
        print(f"Total Students: {Student.totalStudents}")

    @staticmethod
    def is_eligible(age):
        return 18 >= age <= 35 


# s1 = Student(input("Enter the Student Name: ").capitalize(), int(input("Enter the Age: ")))
# s2 = Student(input("Enter the Student Name: ").capitalize(), int(input("Enter the Age: ")))

s1 = Student("Manikanta", 21)
s2 = Student("Aditya", 22)

s1.display()
Student.get_total_students()
print(Student.is_eligible(26))
'''

'''
class Book:
    def __init__(self, BookName, BookAuthor, Price):
        self.name = BookName
        self.author = BookAuthor
        self.price = Price
    
    def display_info(self):
        print(f"Title: {self.name} \nAuthor: {self.author} \nPrice: ₹{self.price}")

# title = input("Enter the Book Title: ").capitalize()
# author = input("Enter the Author of Book: ").capitalize()
# price = int(input("Enter the Book price: "))

# b1 = Book(title, author, price)
b1 = Book("Chandramukhi", "VenkataPathiRaja", 299)
b1.display_info()

'''

'''
class Account:
    def __init__(self, account_holder, pin):
        self.account_holder = account_holder
        self._balance = 0
        self.__pin = pin
    
    def deposit(self, amount):
        self.amount = amount
        print(f"Deposited ₹{self.amount}")
        self._balance += self.amount
    
    def withdraw(self, pin, amount):
        self.pin = pin
        self.amount = amount
        if self.__pin == self.pin:
            if self.amount <= self._balance:
                print(f"Withdraw ₹{self.amount}")
                self._balance -= self.amount
        else:
            print("Incorrect PIN")
        
    def show_balance(self):
        print(f"Avaiable Balance: ₹{self._balance}")

acc = Account("Ravi", 1234)
acc.deposit(5000)
acc.withdraw(1234, 1500)
acc.show_balance()

acc1 = Account(input("Enter Account Holder Name: "), int(input("Enter a 4 digit pin: ")))
acc1.deposit(int(input("Enter Deposit Amount: ")))
acc1.withdraw(int(input("Enter Your pin:")), int(input("Enter Withdraw Amount: ")))
acc1.show_balance()

'''

'''
import random
otp = random.randrange(1000,9999)
print(f"OTP send to your Mobile Number '{otp}'")
class User:
    def login(self,mobileNo, OTP):
        self.mobileNo = mobileNo
        self.otp = OTP
        if otp == self.otp:
            print("User Login in")
        else:
            print("Login Failed")

class Rider(User):
    def book_ride(self):
        print(f"Ride booked successfully")

class Payment(Rider):
    def make_payment(self):
        print("Payment Completed")


ride = Payment()
ride.login(int(input("Enter Mobile Number: ")), int(input("Enter Your OTP: ")))
ride.book_ride()
ride.make_payment()

'''

'''
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

t = Teacher("Sai", 22, "Math")
t.show()
'''

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Sum: ({self.x}, {self.y})")

p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
p3.display()
'''

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        self.email = "bmanikanta@gmail.com"
        print(f"Email sent to {self.email}")

class SMSNotification(EmailNotification):
    def send(self):
        print("SMS sent to registered number")

e = EmailNotification()
s = SMSNotification()
e.send()
s.send()
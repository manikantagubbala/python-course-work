#26.Polymorphism.py -->

#1.Method Overloading (Compile-Time Polymorphism)-->same methods with different parameters

class Method_overload:
    def __init__(self,content=None):
        self.content = content
        return self.content


obj = Method_overload()
print(obj.__init__())
print(obj.__init__("Manikanta"))
print(obj.__init__([1,2,3,4,56]))


#2.Method Overriding (Run-Time Polymorphism) --> same name and parameters but differnt actions

class NormalUser:
    def __init__(self,username):
        self.username = username
        print(f"\nWelcome to Youtube \n{self.username} is created an account")

    def playvideo(self):
        print("Ads Included")
        print("No Background play")
        print("Limited content")

    def Likes(self):
        print("Likes")
    def comment(self):
        print("Comments")
    def Share(self):
        print("Share")

class PremiumUser(NormalUser):
    def __init__(self, username):
        super().__init__(username)

    def playvideo(self):
        print("Ads Free")
        print("Background play")
        print("Unlimited content") 

    
mani = NormalUser("Manikanta")
mani.playvideo()
mani.Likes()
mani.comment()
mani.Share()

aditya = PremiumUser("Aditya")
aditya.playvideo()
aditya.Likes()
aditya.comment()
aditya.Share()


#3. Operator overloading --> using operators with user defined methods


class Number:
    def __init__(self,num):
        self.num = num

    def __str__(self):
        return f"\nNumber: {self.num}"

    def __add__(self,other):
        return f"Addition: {self.num + other.num}"
    
    def __sub__(self,other):
        return f"Subtraction: {other.num - self.num}"
    
    def __mul__(self,other):
        return f"Multiplication: {self.num * other.num}"
    
    def __truediv__(self,other):
        return f"Division: {self.num / other.num}"

    def __lt__(self,other):
        return f"Lessthen: {self.num < other.num}"

    def __gt__(self,other):
        return f"Greaterthen: {self.num > other.num}"

    def __floordiv__(self,other):
        return f"FloorDivision: {self.num // other.num}"

    def __mod__(self,other):
        return f"Modulos: {self.num % other.num}"

    def __pow__(self,other):
        return f"Exponential: {self.num ** other.num}"

    def __equal__(self,other):
        return f"isEqual: {self.num == other.num}"


num1 = Number(90)
num2 = Number(20)

print(num1)
print(num1 + num2)
print(num2 - num1)
print(num1 * num2)
print(num1 / num2)
print(num1 < num2)
print(num1 > num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 == num2)





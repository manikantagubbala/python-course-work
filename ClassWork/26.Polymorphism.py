#26.Polymorphism.py -->

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


class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num + other.num
    
    def __str__(self):
        return f"{self.num}"

    

n=Number(10)
n1=Number(90)
n2=Number(98)

print(n + n2)
print(n)
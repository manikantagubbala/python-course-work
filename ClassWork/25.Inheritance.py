#Single Inheritance -->1 parent class and 1 child class
#Multiple Inheritance -->  More than 1 parent class and 1 child class
#Multilevel Inheritance --> one level to another level (A-B-C)
#Hierarcy Inheritance --> 1 parent class and more than 1 child class

'''
print("Single Inheritance\n")
class A:
    def parent_class(self):
        print("Intialize Parent class")

class B(A):
    def child_class(self):
        print("Intialize Child class")

obj = A()
obj.parent_class()

obj1 =B()
obj1.parent_class()
obj1.child_class()

##########

print("/nMultiple Inheritance\n")
class J:
    def father(self):
        print("Intialize father documents")

class K:
    def mother(self):
        print("Intialize mother gold")
        
class L(J,K):
    def son(self):
        print("Intialize son get both mother and father properties")

j = J()
j.father()

k = K()
k.mother()

l = L()
l.mother()
l.father()

###########


print("\nMultilevel Inheritance\n")
class G:
    def grandfather(self):        
        print("Intialize Grand Father ")
    
class H(G):
    def father(self):
        print("Intialize Father ")

class I(H):
    def mine(self):
        print("Intialize Me")

gf = G()
gf.grandfather()

dad = H()
dad.grandfather()
dad.father()

mani = I()
mani.father()
mani.mine()
mani.grandfather()


#########

print("\nHierarcy\n")
class C:
    def father(self):
        print("Father has debt and also responsbility")

class D(C):
    def daugther(self):
        print("She takes home responsbility")

class E(C):
    def son(self):
        print("He takes debt and clear debt")

c = C()
c.father()

d = D()
d.daugther()
d.father()

e = E()
e.son()
e.father()

'''



#Whatsapp Status

'''
class Status_2015:
    def text(self):
        print("Update Text")

    def image(self):
        print("Update Image")

    def audio(self):
        print("Update Audio")

class Status_2018(Status_2015):
    def emoji(self):
        print('Update Emojies')

    def gif(self):
        print("Update Gif")

class Status_2021(Status_2015):
    def morethan_30_sec(self):
        print("Video can be updated upto 1 min")

    
    def privacy(self):
        print("Updatae Privacy")

class Status_2024(Status_2021,Status_2018):
    def likes(self):
        print("Update Likes")

class Status_2025(Status_2024):
    def mention(self):
        print("Update Mention")

    def Music(self):
        print("Update Music")

eswar = Status_2015()
eswar.text()
eswar.audio()
eswar.image()
print()

venky = Status_2018()
venky.audio()
venky.text()
venky.image()
venky.emoji()
venky.gif()
print()

aditya = Status_2021()
aditya.audio()
aditya.image()
aditya.text()
aditya.morethan_30_sec()
aditya.privacy()
print()

krishna = Status_2024()
krishna.privacy()
krishna.morethan_30_sec()
krishna.likes()
krishna.gif()
krishna.emoji()
krishna.audio()
krishna.text()
krishna.image()
print()

mani = Status_2025()
mani.privacy()
mani.morethan_30_sec()
mani.likes()
mani.gif()
mani.emoji()
mani.audio()
mani.text()
mani.image()
mani.mention()
mani.Music()

'''


#Using Constructor

class Maths:
    def __init__(self,grade):
        self.grade = grade
        print(f"M1 Pass with '{self.grade}' Grade")

class M2:
    def __init__(self,grade):
        self.grade = grade
        print(f"M2 Pass with '{self.grade}' Grade")

class M3:
    def __init__(self,grade):
        self.grade = grade
        print(f"M3 Pass with '{self.grade}' Grade")
        
class PS:
    def __init__(self,grade):
        self.grade = grade
        print(f"P_&_S Pass with '{self.grade}' Grade")

grade = input().upper()
m1 = Maths(grade)

grade = input().upper()
m2 = M2(grade)

grade = input().upper()
m3 = M3(grade)

grade = input().upper()
ps = PS(grade)

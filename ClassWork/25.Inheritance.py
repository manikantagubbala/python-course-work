#Single Inheritance -->1 parent class and 1 child class
#Multiple Inheritance -->  More than 1 parent class and 1 child class
#Multilevel Inheritance --> one level to another level (A-B-C)
#Hierarcy Inheritance --> 1 parent class and more than 1 child class


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
print()
#how to add elemnts in a list.
#list comprehension are nothing but append the elements
'''
#It is not list comprehension
n=int(input("Enter num: "))
l=[]
for i in range(1,n+1):
    l.append(i)
print(l)


s='Python'
u=[i.upper() for i in s if i.islower()]
print(u)

m='123mani4839'
a=[i for i in m if i.isdigit()]
print(a)

b=int(input("Enter num: "))
c={}
for i in range(b):
    if i%2==0:
        c[i]=i*i
print(c)
'''

names=['Manikanta','eswar','Aditya','venky']
upper=[i for i in names if i.istitle()]
print("names: ",upper)


city=['DRM','HYD','KKD','VIZAG']
lower=[i.lower() for i in city]
print("Cities: ",lower)
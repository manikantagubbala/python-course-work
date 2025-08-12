# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
n=int(input())
num1=set(map(int,input().split()))
m=int(input())
num2=set(map(int,input().split()))


c=num1.union(num2)
print(len(c))
'''
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
n=int(input())

for i in range(n):
    b=set(map(int,input().split()))
    
print(a.issuperset(b))


d={
    'name':'Priya',
    'age':31,
}

print(d)
print(d.get('model','Actress'))
print(d)
d.pop('age')
print(d)
print(d.setdefault('age',"Actress"))
print(d)

'''
'''
def countdown(n):
    for i in range(n+1):
        yield n - i
n = 3
for cd in countdown(n):
    print(cd,end=",")
'''

#import math, random

#circle_geometry = []
#radius = 7
#area = math.pi * (radius ** 2)
#circumm=2 * math.pi * radius
#circle_geometry.extend([f"{area:.2f}",f"{circumm:.2f}"])
#print(tuple(circle_geometry))

#random_team=['a','b','c','d','e']
#print(random.choices(random_team,k=3))

#temp = [36,42,39,45,41]
#above = list(filter(lambda i:i>=40,temp))
#print(above)

#def temperature(temp):
#    above = list(filter(lambda i:i>=40,temp))
#    return above
#temp = [36,42,35,45,41]
#print(temperature(temp))

#inputs = ["cat","car","bus","apple"]
#out = list(filter(lambda i:i[0]=='c',inputs))
#print(out)

#fruits=["Apple","apple","Banana","banana","Cherry","cherry"]
#fruit = ""
#for i in fruits:
#    fruit += i.lower()+" "
#out = set(map(lambda i:i,fruit.split()))
#print(list(out))

#def reverse_num(n):
#    if n==0:
#        return 
#    digit = n%10
#    print(digit,end="")
#    reverse_num(n//10)
#reverse_num(12340)


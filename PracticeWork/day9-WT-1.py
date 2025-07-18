#1
'''
m=input("Enter DOB : ").split("-")
m=m[::-1]
print('/'.join(m))
'''
#date,month,year=input().split("-")
#print(f'{year}/{month}/{date}')

#3

#w=input()
#print(w.translate(str.maketrans('aeiou','*****')))

#4
'''
f=list(map(float,input().split()))
print(sum(f))
print(max(f))
'''

#5
'''
credentials = ("admin", "python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("Login successful")
else:
    print("Access deined")
'''
#6

#names=set(input().split(","))
#print(sorted(names))

#7
'''
n=int(input())
d={}
max_marks=0
res_name=' '
for i in range(n):
    name,marks=input().split()
    marks=int(marks)
    d[name]=marks
    if marks>max_marks:
        max_marks=marks
        res_name=name

print(d)
print(res_name)
print(max(d))
print(max(d,key=d.get))
'''

#8

#s=input().split()
#for i in s:
#    print(i[::-1],end=" ")

#9
'''
n=list(map(int,input().split()))
while (0 in n):
    n.remove(0)
print(n)
'''
'''
n=list(map(int,input().split()))
li=[]
for i in n:
    if i!=0:
        li.append(i)

print(li)
'''
#10

s=input()
d={}
for i in s:
    if i not in d and i!=" ":
        d[i]=s.count(i)

print(d)
print()

'''
var = lambda args: statements
var()

s=sorted([(2,3),(4,1),(8,2)], key= lambda i:i[-1])
print(s)

l=['Manikanta','Aditya','Kiran','nani']
m=sorted(l,key= lambda i:i[0],reverse=True)
print(m)

#filter()
l=[1,2,3,43,45,98]
f=list(filter(lambda i : i%2==0, l))
print(f)

l=[0,0,0,0,0,0,0,5,0,67,4,4,5,56666666,0,0,0,5,65,56,7]
f=tuple(filter(lambda i: i!=0, l))
print("Using Tuple: ",f)

s='python'
st=list(map(lambda i:i, s))
print(len(st))

l=['hello','python']
e=list(map(lambda i: len(i),l))
print(e)

a=list(map(int,input().split()))
c=list(map(lambda i:i+i,a))
print(c)



def evenorodd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
evenorodd(int(input()))


lam=lambda n:"Even" if n%2==0 else "Odd"
print(lam(int(input("Enter num: "))))


square=lambda n: n**2
print(square(int(input("Enter num: "))))


add=lambda n,m: n+m
print(add(int(input("Enter num: ")),int(input("Enter num1: "))))


max_num=lambda a,b:a if a>b else b
print(max_num(int(input("Enter num: ")),int(input("Enter num1: "))))


sub=lambda a,b: a-b
print(sub(int(input("Enter num: ")),int(input("Enter num1: "))))
'''

def add(a,b):
    print(a+b)
add(23,456)

#[1,2,3,4]==[0,2,6,12]
n=[1,2,3,4]
ind=list(map(lambda i:i[0] * i[1], enumerate(n)))
print(ind)
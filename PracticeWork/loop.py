print("Control Statements")
'''
print("Fibnooic Series: ")
a,b = 0,1
n=int(input("Enter the size: "))
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    

print("Count Numbers Divisible by 3 (Using for loop)")
n=int(input("Enter Size: "))
c=0
for i in range(n):
    if i%3==0:
        c+=1
print("Count: ",c)


print("Print Multiples of 5 up to N (Using for loop)")
n=int(input("Enter Size: "))
for i in range(5,n,5):
    print(i,end=" ")


print("Find the Maximum of Three Numbers (Using for loop)")
num=input("Enter numbers: ").split()
max_n=num[0]
for i in num:
    if i>max_n:
        max_n=i
print(f'max: {max_n}')


print("Sum of First N Natural Numbers (Using for loop)")
n=int(input("Enter numbers: "))
s=0
for i in range(n):
    s+=i
print(s)


print("Print Numbers from N to 1 (Using while loop)")
n=int(input("Enter numbers: "))
m=0
while n>0:
    print(n)
    n-=1


print("Find Sum of Prime Numbers up to N (Using for loop)")
n=int(input("Enter num: "))
sum=0
for i in range(2,n):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        sum+=i
print(sum)
'''

print("Find the Product of Digits of a Number (Using while loop)")
n=input("Enter number: ")
p=1
for i in n:
    p*=int(i)
print(p)

num=int(input("Enter number: "))
pr=0
while num>0:
    digit = num % 10
    pr += digit
    num //= 10
print(pr)

'''

print("Print Numbers Divisible by Both 3 and 5 (Using for loop)")
n=int(input("Enter number: "))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i)


print("Find GCD of Two Numbers (Using while loop)")
num=int(input("Enter number: "))
num1=int(input("Enter number: "))
gcd=[]
while num1!=0:
    num,num1 = num1,num%num1
print(num)



for i in range(5):
    for j in range(5-i):
        print(".", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

for i in range(5):
    print(" "*(5-i) + "*" * (2*i-1))


for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()



for i in range(1,5):
    for j in range(1,5-i+1):
        print(j,end=" ")
    print()


for i in range(1,5):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(1,2*i+1):
        print(k,end=" ")
    print()

n = 4
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
'''
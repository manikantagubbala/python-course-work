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

'''
print("Find Sum of Prime Numbers up to N (Using for loop)")
n=int(input("Enter num: "))

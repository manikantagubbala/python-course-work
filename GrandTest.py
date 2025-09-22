# GrandTest.py

'''

n = 30
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print(f"{n} is not a Prime Number")
            break
    else:
        print("{n} is a Prime Number")
else:
    print("It is Not a Prime Number")

'''

num = int(input("Enter the Number: "))
count = []
for i in range(2,num):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        count.append(i)
print(len(count))
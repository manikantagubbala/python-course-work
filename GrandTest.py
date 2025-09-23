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



num = int(input("Enter the Number: "))
count = []
for i in range(2,num):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        count.append(i)
print(len(count))

'''

# Patterns
n = 5
print("Pattern - 1")
for row in range(n):
    for col in range(row + 1):
        print(col, end =" ")
    print()


print("\nPattern - 2")
for row in range(1,n):
    for col in range(1,n):
        print(row, end = " ")
    print()

print("\nPattern - 3")
for row in range(1, n):
    for col in range(row):
        print("*", end=" ")
    print()

print("\nPattern - 4")
for row in range(1,n):
    for col in range(n-row):
        print(" ", end=" ")
    for i in range(2*row - 1):
        print("*", end=" ")
    print()

print("\nPattern - 5")
for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

#n=8
#print("\nPattern - 6")
#for row in range(1, n):
#    if row < n//2:
#        for col in range(n - row):
#            print("-", end=" ")
#        for i in range(2*row - 1):
#            print("*", end=" ")
#        print()
#    elif row > n//2:
#        for col in range(row - n//2+1):
#            print("-", end=" ")
#        for i in range(2*(n - row)+1):
#            print("*", end=" ")
#        print()    

'''
n = int(input("Enter number of rows (odd number): "))

mid = n // 2 + 1   # middle row

for row in range(1, n+1):
    if row <= mid:  # upper part (including middle)
        # spaces
        for col in range(mid - row):
            print(" ", end=" ")
        # stars
        for i in range(2*row - 1):
            print("*", end=" ")
    else:           # lower part
        # spaces
        for col in range(row - mid):
            print(" ", end=" ")
        # stars
        for i in range(2*(n - row) + 1):
            print("*", end=" ")
    print()


'''
print("\nPattern - 6")
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0:
            print("*", end=" ")
    print()

print("\nPattern - 7")
for row in range(n):
    print("*", end=" ")

print("\nPattern - 8")
for col in range(n):
    print("*")

print("\nPattern - 9")
for row in range(n):
    for col in range(n):
        if row == n-1 or col == n-1 or row == 0 or col == 0 or col == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("\nPattern - 10")
for row in range(n):
    for col in range(n):
        if row == n-1 or col == n//2 or (row <= n//2 and (row+col == n//2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Letter-'Z'".center(25," "))

n=int(input("Enter the size : "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'Y'".center(25," "))

for i in range(n):
    for j in range(n):
        if (i>=n//2 and j==n//2) or (i<n//2 and (i==j or i+j==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'X'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'W'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i>=n//2 and (i+j==n-1 or i==j)):
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'V'".center(25," "))

for i in range(n):
    for j in range(n *2 - 1):
        if i==j or j== (2 * n - 2 - i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'U'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'T'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'S'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n//2 or (i<n//2 and j==0) or (i>n//2 and j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'R'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or (i<n//2 and j==n-1) or (i>n//2 and i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'Q'".center(25," "))

for i in range(n):
    for j in range(n):
        if (i<n-2 and i==0) or (j<n-2 and j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("Enter the size : "))

print("Letter-'Z'".center(25," "))

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
        if (i==0 and j!=0) or (i==n-1 and j!=n-1) or i==n//2 or (i<n//2 and j==0 and i!=0) or (i>n//2 and j==n-1 and i!=n-1):
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
        if (i==0 and j!=n-1) or (j==0 and i!=n-1) or (j==n-2 and i!=n-1) or (i==n-2 and j!=n-1) or (i>=n//2 and i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'P'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or (i<n//2 and j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()


print("Letter-'O'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'N'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'M'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i<=n//2 and (i==j or i+j==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'L'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'K'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==n//2-1 or (j>n//2 and i+j==n-1) or (i>=n//2 and i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'J'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (i>n//2 and i-j==n//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'I'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'H'".center(25," "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'5'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (i>=n//2 and j==n-1) or (j>=n//2 and i==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'F'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or (j<=n//2 and i==n//2) or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'E'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n//2 or j==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'D'".center(25," "))

for i in range(n):
    for j in range(n):
        if (i==0 and j!=n-1) or j==0 or (i==n-1 and j!=n-1) or (j==n-1 and i!=0 and i!=n-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'C'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("Letter-'B'".center(25," "))

for i in range(n):
    for j in range(n):
        if( i==0 and j!=n-1) or j==0 or (i==n-1 and j!=n-1) or (j==n-1 and i!=0 and i!=n//2 and i!=n-1) or (i==n//2 and j!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("Letter-'A'".center(25," "))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()









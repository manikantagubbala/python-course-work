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

print("\nRightAngleTriangle - Pattern - 3")
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


print("\nOne - Pattern - 10")
for row in range(n):
    for col in range(n):
        if row == n-1 or col == n//2 or (row <= n//2 and (row+col == n//2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nTriangle - Pattern - 11")
for row in range(n):
    for col in range(2*n -1):
        if row == n-1 or (col<=n-1 and row+col == n-1) or (col >= n and col-row == n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("\nPattern - 12")
for row in range(n):
    for col in range(n):
        if (row+col) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

print("\nInverted right-angled triangle - Pattern - 13")
for row in range(n):
    for col in range(n - row):
        print("*", end=" ")
    print()


print("\nReverse Pyramid - Pattern - 14")
for row in range(n):
    for spa in range(row):
        print(" ", end="")
    for col in range(n - row):
        print("*", end=" ")
    print()


print("\nPyramid - Pattern - 15")
for row in range(n+1):
    for spa in range(n - row):
        print(" ", end="")
    for col in range(row):
        print("* ", end="")
    print() 


print("\Floyd’s Triangle - Pattern - 16")
nums = 1
for row in range(n):
    for num in range(row + 1):
        print(nums, end=" ")
        nums += 1
    print()

print("\nPascal’s Triangle - Pattern - 17")
for row in range(n+1):
    for spa in range(n - row):
        print(" ", end="")
    number = 1
    for num in range(row + 1):
        print(f'{number} ', end="")
        number = number * (row - num) // (num + 1)
    print()


print("\nInverted number - Pattern - 18")
for row in range(1,n):
    for col in range(1, n - row + 1):
        print(col, end=" ")
    print()

'''
Diamond pattern:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

Hourglass pattern:
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *

Palindromic number triangle:
    1
   121
  12321
 1234321
123454321

Butterfly pattern:
*       *
* *   * *
* * * * *
* *   * *
*       *

Checkerboard pattern:
* * * * 
 * * * *
* * * *
 * * * *

'''
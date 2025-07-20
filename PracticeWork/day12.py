'''
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

    '''

n=int(input("Enter Number: "))

#for i in range(1,n+1):
#    if i % 2==0:
#        print(f'{i} is an Even Number')

#print("Sum".center(20," "))
#s=0
#for i in range(n+1):
#    s+=i
#
#print(f'Sum of n numbers is {s}')

#print("Factorial".center(20," "))
#f=1
#for i in range(1,n+1):
#    f*=i
#
#print(f'Factorial Number of {n} is {f}')

#print("Table".center(20," "))
#for i in range(1,21):                       #Table(7)
#    print(f'{n} * {i} = {n*i}')

#print("Prime Number".center(25," "))
#if n>1:
#    for i in range(2,n):
#        if n%i==0:
#            print(f'{n} is not a Prime Number')
#            break
#    else:
#        print(f'{n} is Prime Number')
#else:
#    print(f'{n} is not a Prime Number')


#print("Count Numbers".center(20," "))
#c=0
#for i in range(n):
#    if i%3==0:
#        c+=1
#print(f'Count: {c}')

#print("Num Palindrome".center(20," "))
#n=input("Enter Number:").strip()
#while n.isdigit():
#    if n==n[::-1]:
#        print(f'{n} is Palindrome')
#        break
#    else:
#            print(f'{n} is not a Palindrome')
#            break
#else:
#    print(f'{n} is not a Palindrome')


#print("Multiplies of num".center(20," "))
#for i in range(1,n):
#    if 5%i==0 or i%5==0:
#        print(i)
#
#n = int(input("Enter a number: "))
#
#print("Multiples of 5 up to", n, "are:")
#for i in range(5, n + 1, 5):
#    print(i, end=" ")



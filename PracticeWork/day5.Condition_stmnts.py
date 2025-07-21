#print("Even or Odd".center(20," "))
#a = int(input())
#if a%2==0:
#    print("Even")
#else:
#    print("Odd")


#a = int(input("Enter number : "))
#if a>0:
#    print("Positive")
#elif a<0:
#    print("Negative")
#else:
#    print("Zero")

print("Leaf Year".center(30)," ")
year=int(input("Enter number : "))
if year%400==0 or year%4==0 and year%100!=0  :
    print(f'{year} is Leaf year')
else:
    print(f'{year} is not a Leaf year')

    
#print("Divisible".center(20," "))
#num=int(input("Enter your number :"))
#if num%5==0:
#    print(f'{num} is divisible by 5')
#else:
#    print(f'{num} is not divisible by 5')

#print("Divisible".center(20," "))
#num=int(input("Enter your number :"))
#if num%3==0 and num%7==0:
#    print(f'{num} is divisible by both 3 and 7')
#elif num%3==0:
#    print(f'{num} is divisible by 3')
#elif num%7==0:
#    print(f'{num} is divisible by 7')
#else:
#    print(f'{num} is not divisible by both 3 and 7')

#print("Check if number is 3-digit".center(40," "))
#num=int(input("Enter number : "))
#if num>=100 and num<=999:
#    print("3-digit number")
#else:
#    print("It is not a 3-digit number")

print("vowel".center(15," "))
s=input("Enter a character : ").lower()
if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
    print(f'{s} is vowel')
else:
    print(f'{s} is not a vowel.')


#print(" ")
#print("or".center(10," "))
#s=input("Enter a character : ").lower()
#if s=='a':
#    print(f'{s} is vowel')
#elif s=='e':
#    print(f'{s} is vowel')
#elif s=='i':
#    print(f'{s} is vowel')
#elif s=='o':
#    print(f'{s} is vowel')
#elif s=='u':
#    print(f'{s} is vowel')
#else:
#    print(f'{s} is not a vowel.')

#print("Greater".center(20," "))
#num=int(input("Enter your number :"))
#n=int(input("Enter your number :"))
#if num<n : 
#    print(f'{n} is greater number')
#else:
#    print(f'{num} is greater number')

#print("Smaller".center(20," "))
#num=int(input("Enter your number :"))
#n=int(input("Enter your number :"))
#if num<n : 
#    print(f'{num} is smaller number')
#else:
#    print(f'{n} is smaller number')

#print("zero".center(20," "))
#num=int(input("Enter your number :"))
#if num==0 : 
#    print(f'{num} is zero')
#else:
#    print(f'{num} is not zero')

#print("multiple".center(20," "))
#num=int(input("Enter your number :"))
#if num%10==0:
#    print(f'{num} is multiple by 10')
#else:
#    print(f'{num} is not multiple by 10')

#print("Vote".center(20," "))
#num=int(input("Enter your number :"))
#if num>=18:
#    print(f'Eligible to vote')
#else:
#    print(f'You are not eligible to vote.')

#print("range".center(15," "))
#num=int(input("Enter number : "))
#if num>=1 and num<=100:
#    print(f'{num} is in range.')
#else:
#    print(f'{num} is not in  range.')

#print("Square".center(15," "))
#num=int(input("Enter number1 : "))
#n=int(input("Enter number2 : "))
#if n**2==num:
#    print(f'{num} is a square of {n}')
#else:
#    print(f'{num} is not a square of {n}')

#print("Strings are equal".center(30," "))
#s=input("Enter your string1 : ").lower()
#m=input("Enter your string2 : ").lower()
#if s==m:
#    print(f'{s} and {m} are equal')
#else:
#    print(f'{s} and {m} are not equal')



#print("Prime".center(10," "))
#n=int(input("Enter number : "))
#if n%2!=0 and n%n==0 and n!=1 or n==2:
#    print("Prime")
#else:
#    print("NP")

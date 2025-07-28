'''
print("Check if a number is a 4-digit even number")

n=input("Enter Number: ").strip()
if len(n)==4:
    n=int(n)
    if n%2==0 :
        print(f'{n} is 4-digit even number')
    else:
        print(f'{n} is 4-digit odd number')
else:
    print(f'{n} is not 4-digit number')

n=int(input("Enter: "))
if n>999 and n<=9999:
    if n%2==0:
        print(f'{n} is 4-digit even number')
    else:
        print(f'{n} is 4-digit odd number')
else:
    print(f'{n} is not 4-digit number')


print("Check if a character is a consonant")
s=input("Enter a character: ").lower()
if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
    print(f'{s} is not a consonant')
else:
    print(f'{s} is a consonant')


print("Check if a string starts with a vowel")
w=input("Enter a word: ").lower()
if w[0]=='a' or w[0]=='e' or w[0]=='i' or w[0]=='o' or w[0]=='u' :
    print(f'{w} starts with vowel')
else:
    print(f'{w} starts with consonant')



print("Check if three sides form a valid triangle")
t=input("Enter triangle three sides: ").split(",")
if len(t)==3:
    print("Valid Triangle")
else:
    print("Not a valid Triangle")


print("Find the greatest among three numbers")
n=input("Enter numbers: ").split(",")
print(max(n))


print("Check if a year is a century year and leap year")
year=int(input("Enter year: "))
if  year%400==0 or year%4==0 and year%100!=0:
    print(f'{year} is a leaf Year')
else:
    print(f'{year} is not a leaf year')

    

print("Check if a character is a digit")
ch=input("Enter character: ")
if ch.isdigit()==True:
    print(f'{ch} is a digit')
else:
    print(f'{ch} is not a digit')


print("Check if a number is palindrome (integer)")
n=input("Enter Number: ")
if n==n[::-1]:
    print("It is a palindrome")
else:
    print("It is not a Palindrome")


print("Check if a number is palindrome (integer)")
s1,s2=input("Enter two strings: ").split()
if len(s1)>len(s2):
    print(f'first string is longer')
else:
    print("Second string is longer")



print("Check if a number is within a specific range (50 to 100) and divisible by 5")
n=int(input("Enter number: "))
if n>=50 and n<=100 and n%5==0:
    print("In range and divisible by 5")
else:
    print("Not In range and divisible by 5")

    

print("Validate if a password length is strong (8 or more characters)")
password=input("Enter your password: ")
if len(password)>=8:
    print("Strong password")
else:
    print("weak password")



print("Check if sum of two numbers is even")
a=list(map(int,input("Enter numbers: ").split()))
if sum(a)%2==0:
    print("Sum is Even")
else:
    print("Sum is Odd")
    


print("Check if the character is a special symbol (!, @, #, etc.)")
c=input("Enter a character: ")
if c.isalnum():
    print(f'{c} is not a Special Character')
else:
    print(f'{c} is a Special character')



print("Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)")
temp=int(input("Enter Room Temperature: "))
if temp<=15:
    print(f'Cold')
elif temp>15 and temp<=30:
    print("Moderate")
else:
    print("Hot")


print("Check if a number lies outside the range 10 to 50")
n=int(input("Enter Number: "))
if n>=10 and n<=50:
    print(f'{n} is inside the range')
else:
    print(f'{n} is outside the range')
    

    
print("Compare two ages and determine who is older or if same age")
n=int(input("Enter Number: "))
m=int(input("Enter Number: "))
if n>m:
    print(f'{n} is older')
else:
    print(f'{m} is older')
    


print("Check if an angle is acute, right, or obtuse")
n=int(input("Enter an Angle: "))
if n<90:
    print(f'{n} is Acute angle')
elif n==90:
    print(f"{n} is Right angle")
elif n>90 and n<180:
    print(f'{n} is obtuse angle')
elif n==180:
    print(f'{n} is Straight angle')
else:
    print(f"{n} is not an angle")

'''

print("Check if number is a perfect square (basic method)")
n=int(input("Enter a Square number: "))
is_square=False
for i in range(1,n):
    if i*i==n:
        is_square=True
        break
if is_square:
    print(f"{n} is perfect square")
else:
    print(f"{n} is not perfect Square")


n=int(input())
s=0
while n>0:
    s+= (n%10)
    n=n//10
print(s)
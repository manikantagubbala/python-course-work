
'''
print("Streak")

n=list(map(int,input("Enter steaks : ").split()))
cs=0
ls=0
for i in n:
    if i==1:
        cs+=1
        if cs>ls:
            ls=cs
    else:
        cs=0

print(ls)
print(cs)



print("ATM")
stored_pin='1234'
n=int(input("Enter size: "))
for i in range(n):
     pin=input("Enter your PIN: ")
     if pin==stored_pin:
          print("Login Successfull")
          break
     else:
          print("PIN Incorrect")
else:
     print("ATM Blocked")

'''

print("Find Sum of Prime Numbers up to N (Using for loop)")
print()
'''
i=int(input("Enter number: "))
if i>-10 and i<=9:
    print("Single digit ")
elif 10<=i<=99 or i<-9 or i<-100:
    print("Double digit")
else:
    print("More tha double digit")


'''


#a=int(input("Enter number1: "))
#b=int(input("Enter number2: "))
#c=int(input("Enter number3: "))

l=list(map(int,input().split()))
print(sorted(l))
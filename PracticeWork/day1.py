
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
print("Pattern".center(20,"*"))
for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print()

print()

for i in range(5):
    for j in range(5-i):
        print('*',end=" ")
    print()

print()
for i in range(5):
    for j in range(i):
        print(' ',end=" ")
    for k in range(5-i):
        print("*",end=" ")
    print()

print()
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print('*',end=" ")
    print()

'''
print()
n=int(input("Enter size: "))
for i in range(n):
    if i<=n//2:
        for j in range(i+1):
            print('*',end=" ")
        print()
    else:
        for k in range(n-i):
            print('*',end=" ")
        print()


print()
n=int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            print("0", end=" ")
        else:
            print('1', end=" ")
    print()
    

t=int(input("Enter total Bill:"))
if t>=0 and t<=999:
    print(f'Total Bill: {t}')
elif t>=1000 and t<=4999:
    d=(t/100)*5
    print(f'Total Bill: {t-d}')
elif t>=5000 and t<=9999:
    d=(t/100)*10
    print(f'Total Bill: {t-d}')
else:
    d=(t/100)*15
    print(f'Total Bill: {t-d}')
    


gym={
    1:{'phase':'monthly','fee':500},
    2:{'phase':'quarterly','fee':1300},
    3:{'phase':'yearly','fee':5000}
}
choice=int(input("Enter one choice in gym: "))
n=int(input("Enter no.of people: "))

if choice in gym:
    print(gym[choice]['fee'] * n)


Our_PIN='1234'
attempt=0
max_attempts=3
while attempt<max_attempts:
    pin=input("Enter your PIN: ").strip()
    if Our_PIN==pin and len(pin)==4:
        print("Access Granted")
        break
    else:
        print("Your PIN is incorrect")
        attempt+=1
else:
    print("ATM Blocked.TRY again Later.")



n=int(input("Enter your members: "))
l=[]
for i in range(n):
    aud=int(input("Enter mem line by line : "))
    l.append(aud)    
print(l)

price=0
for i in l:
    if i<=5:
        price+=0
    elif i>5 and i<=18:
        price+=100
    elif i>=19 and i>=60:
        price+=150
    else:
        price+=120
print(price)
'''

n=int(input("Enter seats: "))
s=[]
for i in range(n):
    seat=input("Enter seat: ")
    s.append(seat)
print(f'Total Seats: {s}')

b_seats=[]
b=int(input("How many tickets u want: ")) 
for i in range(b):
    choose=input("Enter seats: ")
    if choose in s:
        b_seats.append(choose)
        s.remove(choose)
print(f'Booked Seats: {b_seats}')
print(f'Available Seats: {s}')

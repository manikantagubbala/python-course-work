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
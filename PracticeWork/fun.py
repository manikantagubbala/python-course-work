"""print("Function")

def add():
    return a+b
def sub():
    return a-b
def mul():
    return a*b
def div():
    return a/b
def fd():
    return a//b
def mod():
    return a%b

a=int(input())
b=int(input())


while True:
    print()
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.floor division")
    print('6.modulus')
    print("0.Exit")

    op=int(input("Enter calculation number: "))
    if op==0:
        print("0")
        break
    elif op==1:
        print(add())
    elif op==2:
        print(sub())
    elif op==3:
        print(mul())
    elif op==4:
        print(div())
    elif op==5:
        print(fd())
    elif op==6:
        print(mod())
        
"""
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)
def fd():
    print(a//b)
def mod():
    print(a%b)

a=int(input())
b=int(input())


while True:
    print()
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.floor division")
    print('6.modulus')
    print("0.Exit")

    op=int(input("Enter calculation number: "))
    if op==0:
        print("0")
        break
    elif op==1:
        add()
    elif op==2:
        sub()
    elif op==3:
        mul()
    elif op==4:
        div()
    elif op==5:
        fd()
    elif op==6:
        mod()
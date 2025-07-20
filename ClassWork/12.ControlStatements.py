#12.ControlStatements.py
#print("For Loop".center(20," "))
#num=int(input("Enter the table number : "))
#
#for i in range(1,21):
#    print(f'{num} * {i} = {num*i}')


#s=input("Enter name : ").split()
#for i in s:
#    print(f'The length of {i} is',len(i))

#name='Manikanta adithya Sheshu'.lower()
#n=len(name)
#ch=input("Enter the chacter in name:").lower()
#
#for i in range(n):
#    if name[i] == ch:
#        print(f'The index value of {name[i]} is {i}')
#else:
#    print(f'{ch} is not in name')

#products = ['cycle', 'mobile', 'watch', 'mouse']
#fitem=input("Enter you need product : ").split()
#
#for i in fitem:
#    if i in products:
#        print(f'{products.index(i)} {i}')
#    else:
#        print(f'{i} is not available.')
#

n=int(input("Enter Number: "))

if n>1:
    for i in range(2,n):
        if n % i == 0:
            print(f'{n} is not a Prime Number.')
            break
    else:
        print(f'{n} is a Prime Number.')
else:
    print(f'{n} is not a Prime Number')
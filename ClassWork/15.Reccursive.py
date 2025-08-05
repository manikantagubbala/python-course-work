print()
'''
def display(s,ind):
    if ind==len(s):
        return 
    print(s[ind])
    return display(s,ind+1)
s="Python Programming"
display(s,0)


def display(s,ind):
    if ind==-1:
        return
    print(s[ind],end="")
    display(s,ind-1)
s="python"
display(s,len(s)-1)
print()


def sod(n):
    if n<=0:
        return n
    return (n%10) + sod(n//10)
print(sod(int(input("Enter number: "))))
'''

print('Pass by value: \n')
'''
Pass by value can apply only immutable objects.(int, string, tuple, float)
'''

'''
print("pass by value(int, float)")
def pas(a):
    a=a+10
    print("Inside of the function: ",a)
a=20.5
pas(a)
print("Outside of the function: ",a)

print("pass by value(string)")
def str_modi(s):
    s+=" manikanta"
    print("Inside of the function: ",s)
s='bhuvana'
str_modi(s)
print("Outside of the function: ",s)

print("pass by value(tuple)")
def tup_modi(t):
    t+=(33,18)
    print("Inside of the function: ",t)
t=(12,15,10)
tup_modi(t)
print("Outside of the function: ",t)

print("Pass by reference: ")
'''
#Pass by reference is only possible in immutable: (lists, sets, dictionary)

'''

print("pass by reference(list): ")

def pas_ref(l):
    l.append(89)
    print("Inside of the function: ",l)
l=[1,2,3,4,4]
pas_ref(l)
print("Outside the function: ",l)

print("Shallow copy: (effects the inside of function but can't effect the  original function)")
def lis_ref(li):
    li=li.copy()
    li.append(89)
    print("Inside of the function: ",li)
li=[1,2,3,4,4]
lis_ref(li)
print("Outside the function: ",li)

print("pass by reference(set)")
def se_ref(st):
    st.add(33)
    print("Inside of the function: ",st)
st={1,2,3,43,2,43}
se_ref(st)
print("Outside of the function: ",st)

print("pass by reference(dictionary)")
def di_ref(d):
    d[4]=16
    print("Inside of the function: ",d)
d={1:1,2:4,3:9}
d[5]=25
di_ref(d)
print("Outside of the function: ",d)


'''

#def reverse(s,ind):
#    if ind==len(s):
#        return 
#    reverse(s,ind+1)
#    print(s[ind],end="")
#s=input("Enter a string: ")
#reverse(s,0)


#n=123
#s=0
#while n>0:
#    s+= (n%10)
#    n=n//10
#print("Sum of n: ",s)


#def sumofdigit(n):
#    if n==0:
#        return n
#    return n%10 + sumofdigit(n//10)
#print(sumofdigit(int(input("Enter num: "))))

print("hello")

#def product(n):
#    if n==0:
#        return 1
#    return n%10 * product(n//10)
#print(product(int(input("Enter number: "))))


#def fac(n):
#    if n==0:
#        return 1
#    return n * fac(n-1)
#print(f'Factorial: {fac(5)}')


#print("Reverse string: ")
#def reverse(s,ind):
#    if ind==len(s):
#        return
#    reverse(s,ind+1)
#    print(s[ind],end='')
#s='python'
#reverse(s,0)

'''
print("\nFibnoicc: ")
n,m=0,1
a=5
for i in range(a+1):
    print(m,end=" ")
    n,m=m,n+m

def fib(num):
    if num<=0:
        return 0
    elif num==1:
        return 1
    return fib(num-1)+fib(num-2)
    
num=int(input("Enter number: "))
for i in range(1,num+1):
    print(fib(i),end=" ")


def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)
n=5
print(fac(n))


def reverse(s,i):
    if i==len(s):
        return 
    reverse(s,i+1)
    print(s[i],end='')
s='apple'
reverse(s,0)


def count_digits(n):
    if n==0:
        return 0 
    return 1+count_digits(n//10)
print(count_digits(8978411298))


def power(base,exp):
    if exp==0:
        return 1
    return base**exp
print(power(3,1))



h=[24,18]
print(max(h))

def gcd(n,num):
    m=[n,num]
    a=[]
    for i in range(1,max(m)+1):
        if n%i==0 and num%i==0:
            a.append(i) 
    return max(a)
n=int(input("Enter num: "))
num=int(input("Enter num: "))
print("GCD: ",gcd(n,num))

'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(24,18))

print(48 % 18)
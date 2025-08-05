
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

#l=list(map(int,input().split()))
#print(sorted(l))

'''
a=list(map(str,input("Enter inputs: ").split()))
print(a)
d={}
count=0
for i in a:
    if i not in d and i!=" ":
        d[i]=a.count(i)
    
print(d)


def dic_ount(text):
    h={}
    for i in text:
        if i not in h and h!=" ":
            h[i]=text.count(i)
    return h
text=input("Enter strings: ").split()
print(dic_ount(text))

'''

def is_anagram(a,b):
    for i in a :
        if i in b:
            return True
    else:
        return False


a='apple'
b='ple'
print(is_anagram(a,b))

a=[1,2,3,4,5,6]
even=list(filter(lambda i:i%2==0,a))
print(even)

def email(f,l,d):
    mail=f+"."+l+"."+d
    return mail
f='mani'
l='kanta'
d='com'
print(email(f,l,d))

print()
'''
a=[[1,2],[3,4],[8]]
b=[]
c=[]
b.append(a[0][0])
b.append(a[0][1])
b.append(a[1][0])
b.append(a[1][1])
print(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        c.append(a[i][j])

print(c)
'''

#a=[[1],[2,3],[4]]
#print(a[0][0])
#print(len(a[2]))
'''
def is_anagram(s1,s2):
    if len(s1)>len(s2) or len(s1)<len(s2):
        return False
    else:
        return True
s1,s2=input("Enter: ").split()
print(is_anagram(s1,s2))


def f_matrix(matrix):
    a=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            a.append(matrix[i][j])
    return a
matrix=eval(input())
print(f_matrix(matrix))


def f_matrix(m):
    a=[]
    for i in m:
        for j in i:
            a.append(j)
    return a
m=eval(input())
print(f_matrix(m))

k=[]
l=[[1],[2,3],[4]]
for i in l:
    for j in i:
        k.append(j)
print(k)


def sum_of_digits(n):
    if n==0:
        return n
    return n%10 + sum_of_digits(n//10)
print("sumOfDigits: ",sum_of_digits(234))

def power(bases,exp):
    if exp<=0:
        return 1
    return bases**exp
bases=int(input("Enter num: "))
exp=int(input("Enter num: "))
print(power(bases,exp))



def is_anagram(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if sorted(s1)==sorted(s2):
        return True
    else:
        return False
s1,s2=input("Enter values: ").split()
print(is_anagram(s1,s2))
'''

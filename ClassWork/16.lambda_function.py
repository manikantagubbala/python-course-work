print()

'''
var = lambda args: statements
var()

'''

'''
s=sorted([(2,3),(4,1),(8,2)], key= lambda i:i[-1])
print(s)

l=['Manikanta','Aditya','Kiran','nani']
m=sorted(l,key= lambda i:i[0],reverse=True)
print(m)

#filter()
l=[1,2,3,43,45,98]
f=list(filter(lambda i : i%2==0, l))
print(f)

l=[0,0,0,0,0,0,0,5,0,67,4,4,5,56666666,0,0,0,5,65,56,7]
f=tuple(filter(lambda i: i!=0, l))
print("Using Tuple: ",f)

s='python'
st=list(map(lambda i:i, s))
print(len(st))

l=['hello','python']
e=list(map(lambda i: len(i),l))
print(e)

a=list(map(int,input().split()))
c=list(map(lambda i:i+i,a))
print(c)



def evenorodd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
evenorodd(int(input()))


lam=lambda n:"Even" if n%2==0 else "Odd"
print(lam(int(input("Enter num: "))))


square=lambda n: n**2
print(square(int(input("Enter num: "))))


add=lambda n,m: n+m
print(add(int(input("Enter num: ")),int(input("Enter num1: "))))


max_num=lambda a,b:a if a>b else b
print(max_num(int(input("Enter num: ")),int(input("Enter num1: "))))


sub=lambda a,b: a-b
print(sub(int(input("Enter num: ")),int(input("Enter num1: "))))


def add(a,b):
    print(a+b)
add(23,456)


a=eval(input("Enter numbers: "))
sq=list(map(lambda i:i*i ,a ))
print(sq)


a={1,2,3,4,5,5}
f=set(filter(lambda i:i%2!=0,a))
print("filter: ",f)


a=[0,0,0,8,8,5,4,23,45,65,23,2,60,7,7,76,90,0,0,0,0,5,6,345,3,0]
f=tuple(filter(lambda i:i!=0,a))
print("Remove Zeroes: ",f)


a=[1,2,3,4]
f=list(map(lambda i:i+3,a))
print(f)


data={'Mani':85,'Aditya':75,'Eswar':728}
s=dict(sorted(data.items(),key=lambda i:i[0]))
print("Sorted data: ",s)

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
so=sorted(students,key=lambda i:i[0])
print(so)


print(sorted(data.items()))

a=list(map(int,input().split()))
b=[1,2,3,4]
'''

#n=int(input())
#s=lambda n:n*n
#print(s(n))

#Reduce in lambda
a=[1,2,3,4,5]
print("sumofnums: ",sum(a))


#n=int(input("Enter number: "))
#iseven=lambda n:True if n%2==0 else False
#print("EvenOrOdd: ",iseven(n))

maximum=lambda a,b:a if a>b else b
print("maximunOfTwoNumbers: ",maximum(54,478))

multiply=lambda a,b:a*b
print("multiplyOfTwoNum: ",multiply(5,8))

a=[(2,1),(43,4),(55,2)]
sortOfList=sorted(a,key=lambda i:i[1])
print("AscendingOrder: ",sortOfList)

reverseSort=sorted(a,key=lambda i:i[1], reverse=True)
print("descendingOrder: ",reverseSort)

a=[1,2,3,4,5,6,67,7,8,9]
evennum=list(filter(lambda i:i%2==0,a))
print("EvenNumbers: ",evennum)

square=list(map(lambda i:i*i,a))
print("SquareOfNumbers: ",square)

a=['hello','python']
upper=list(map(lambda i:i.upper(),a))
print("changeToUpper: ",upper)

a=[{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}]
order=sorted(a,key=lambda i:i['age'])
print("AscendingOrderFromkeys: ",order)

a='hello'
length=lambda a:len(a)
print("LengthOfTheString: ",length(a))

stWithVowel=lambda a:True if a[0]=='a'or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u' else False
print("StartWithVowelOrNot: ",stWithVowel(a))

s=lambda a:True if a[0] in 'aeiou' else False
print("StartWithVowelOrNot: ",s(a))

a=[1,2,3,4,-5]
add10=list(map(lambda i:i+10,a))
print("Add10OfListOfNum: ",add10)

a=['hello','a','mani','cat']
morethan3=list(filter(lambda i:len(i)>3,a))
print("Filter strings longer than 3 characters: ",morethan3)
#10.1.InputFormatting.py
#print("Integer".center(15,' '))
#i=int(input("Enter int value : "))
#print(type(i))

#print("Float".center(15,' '))
#f=float(input("Enter float value : "))
#print(type(f))

#print("String".center(15,' '))
#s=input("Enter string value : ")
#print(type(s))

#print("List".center(15,' '))
#l=input("Enter your list : ").split()
#print(l)
#print(type(l))

#l=input("Enter your list : ")
#print(l)

#l=list(map(int, input("Enter values : ").split()))
#print(l)
#print(type(l))

#print("Tuple".center(15,' '))
#t=input("Enter tuple values : ")
#print(t)
#
#t=input("Enter tuple values : ").split()
#print(t)
#
#t=tuple(map(int,input("Enter Tuple values : ").split()))
#print(t)
#
#t=tuple(map(str,input("Enter Tuple values : ").split()))
#print(t)

#print("Set".center(15,' '))
#s=set(map(str,(input("Enter Values : "))))
#print(s)
#
#s=set(map(str,input("Enter values : ").split()))
#print(s)

#print("Dictionary".center(15,' '))
#student=eval(input("Enter your student details : "))
#print(student)

print("Multiple Inputs with Unpacking ".center(75," "))
username,password = input("Enter your username and password : ").split()
print("username : ", username)
print("password : ", password)
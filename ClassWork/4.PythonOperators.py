#4.PythonOperators.py

#1.Arithmetic Operators

a=30
b=10
print("        Arithmetic Operators")
print("Addition(+):", a+b)           #Addition(+): 40
print("Subtraction(-):", a-b)        #Subtraction(-): 20
print("Multiplication(*):", a*b)     #Multiplication(*): 300
print("Division(/):", a/b)           #Division(/): 3.0
print("Division(/):", b/a)           #Division(/): 0.3333333333333333
print("FloorDivision(//):", a//b)    #FloorDivision(//): 3
print("Modulus(%):", a%b)            #Modulus(%): 0
print("Exponential(**):", a**b)      #Exponential(**): 590490000000000

#2.Comparison Operators

print("       Comparison Operators:")
print("Equal To():",a==b)                   #Equal To(): False
print("Not Equal To():",a!=b)               #Not Equal To(): True
print("Greater than():",a>b)                #Greater than(): True
print("less than():",a<b)                   #less than(): False
print("Greater than or Equal To():",a>=b)   #Greater than or Equal To(): True
print("less than or Equal To():",a<=b)      #less than or Equal To(): False

#3.Assignment Operator

print("         AssignmentOperator")
c=10                 #10=c
c+=10                #20=c
print("Add & Assign:",c)                  #Add & Assign: 20
c-=10                #10=c
print("Sub & Assign:",c)                 #Sub & Assign: 10
c/=5                 #2.0=c
print("Div & Assign:",c)                 #Div & Assign: 2.0
c=10                 #10=c
c//=5                #2=c
print("Floor Div & Assign:",c)           #Floor Div & Assign: 2
c*=5                 #10=c
print("Mul & Assign:",c)                 #Mul & Assign: 10
c**=10               #10000000000=c
print("Exponential & Assign:",c)         #Exponential & Assign: 10000000000



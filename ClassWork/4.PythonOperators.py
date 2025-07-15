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

#4.Logical Operators
#4.1."AND" If All conditions are TRUE then only print TRUE Otherwise FALSE
#4.2."OR" If one of the condition is TRUE then print TRUE Otherwise FALSE
#4.1."NOT" If the statement is TRUE it prints FALSE If the statement is FALSE it prints TRUE 

x=10 
y=20
print("AND : ",x==y and x<y)         #AND :  False
print("OR : ",x==y or x<y)           #OR :  True
print("NOT : ",not(x==y))            #NOT :  True

#5.MemberhsipOperators
#In this operator using "in" and "not in".It can be used in Senquential Datatypes : LISTS,TUPLE,SETS.
#In-->Returns True if the value exists in the sequence
#Not In-->.Returns True if the value does NOT exist in the sequence

d = {
    'name':'tarak',
    'age':40,

    'name':'arjun',
    'age':41

}
print(type(d))                        #dict
print("NOT IN:",'tarak' not in d)     #True
print("IN:",'name' in d)              #True

fav_movies = ["Darling","Temper","Businessman","Badri"]
print("NOT IN:",'Darling' not in fav_movies)     #False
print("IN:",'Badri' in fav_movies)               #True
print(type(fav_movies))                          #list

#6.IdentityOperators
#It can exits same path (is)
#It can't exits same path (is not)

m=[1,2,5,4]
n=[1,2,5,4]
print("IS:", m is n)            #False
print("IS NOT:", m is not n)    #True

k=m
print("IS:",m is k)             #True

print(id(m))                #138796659265728
print(id(n))                #138796657115008
print(id(k))                #138796659265728


#7.BitwiseOperators

x=4                                 #Binary= 0 1 0 0
y=6                                 #Binary= 0 1 1 0
                                             
print("AND(&):", x&y)               # 0 1 0 0 = 4
print("OR(|):", x|y)                # 0 1 1 0 = 6
print("XOR(^):", x^y)               # 0 0 1 0 = 2       Opposite reactions can be True
print("NOT(~):", ~x)                #  [~n = -(n + 1)]
print("NOT(~):", ~y)                #  [~n = -(n + 1)]

 
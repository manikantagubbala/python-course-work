#2.variablesRulesAndAssignments.py

myvar = 10     # valid var
myVar = 20     # valid var
MYVAR = 30     # valid var
my_Var = 40    # valid var
my_var1 = 50   # valid var
print(my_var1, my_Var, myVar, myvar, MYVAR) # 50, 40, 20, 10, 30

a, b ,c = 1,2,3   #Multiple Assignment  
print(a, b, c)    #1, 2, 3

a, b = b, a     #Swaping
print(a)        # 2
print(b)        # 1

a = b = c = 100   #Assigning same values
print(a, b, c)    # 100 100 100 

m = "nani"       #VariableAssignment
del m            #delete the value

name = "Manikanta"    #Assigning the value
print(name)           # Manikanta


'''
#          = comment
myVar      = identifier
=          =  operator
10         = literal
print()     = identifier
a           = identifier
b           = identifier
c           = identifier
m           = identifier
"nani"       = literal
del           = keyword
name           = identifier
"Manikanta"     =  literal
'''


print("Hello World!") #Hello World!
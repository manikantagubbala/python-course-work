print("Module is a grp of functions ")
#import functions
import functions as fun

a=int(input("Enter a: "))
b=int(input("Enter b: "))
op=input("Enter any operator: (+,-,*,/) ")


if op=='+':
    fun.add(a,b)
elif op=='-':
    fun.sub(a,b)
elif op=='*':
    fun.mul(a,b)
elif op=='/':
    fun.div(a,b)
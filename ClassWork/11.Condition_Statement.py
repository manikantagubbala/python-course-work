#12.condition_statement.py
''''

                    'Simple if'
if condition : 
    #if-True-statements


                    "if-else"
if condition : 
    #if-True-statement
else:
    #False-statement

                    "If-elif-else"
if condition-1:
    #cond-1 stmts
elif cond-2:
    #cond-2 stmts
elif cond-3:
    #cond-3 stmts
.
.
.
elif cond-n:
    #cond-n stmts
else:
    #False stmts


                     "Nested if"
if cond-outer:
    if cond-inner:
        #if-True stmts
    else:
        #if-false stmts
else:
    #false stmts

'''

#If cond
#s=input("Enter your signal color (R O G) : ")






#If-Else Cond

#items=['shoes','tv','phone','laptop']
#print("Welcome to Store".center(50," "))
#searchitem=input("Enter your item : ").lower()
#
#if searchitem in items:
#    print(f'{searchitem} found. Buy now!!')
#else:
#    print(f'{searchitem} is not found. Please come the store after two days.')
#

#elif cond
#print("Welcome to my weekend plan ".center(120,'-'))
#amount=int(input("Enter your amount : "))
#
#if amount>=10000:
#    print("Go to Goa Trip")
#elif amount>=5000:
#    print("Go for Shopping")
#elif amount>=2000:
#    print("Go for a movie in imax")
#elif amount>=500:
#    print("Looking for a Biryani")
#else:
#    print("You can save money and sleep now.!")


print("Result".center(25," "))
data={
    1:{'name': 'Manikanta', 'attempt_status' : False, 'python' : 0, 'sql' : 0},
    2:{'name': 'Aditya', 'attempt_status' : True, 'python' : 70, 'sql' : 80},
    3:{'name': 'Eswar', 'attempt_status' : True, 'python' : 50, 'sql' : 60},
    4:{'name': 'Venky', 'attempt_status' : True, 'python' : 40, 'sql' : 35},
}

stid=int(input("Enter Student Id : "))

if data[stid]['attempt_status']:
    total=data[stid]['python']+data[stid]['sql']
    print(total)







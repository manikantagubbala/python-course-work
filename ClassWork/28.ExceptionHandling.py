#28.ExceptionHandling.py

try:
    a+=10
except NameError:
    print("a is not defined\n")


l=[1,23,4,5,6]
try:
    l[9]
except:
    print("You have entered the out of range value\n")


#try:
#    num = int(input("Enter the number: "))
#except ValueError: 
#    print('Enter the proper data type')

try: 
    d={1:2,3:4}
    print(d[1])

    f= 1+"mani"
except (NameError,KeyError,TypeError) as e:
    print(f"You can error in this program {e}\n")

try:
    b=[10]
    b.append(1)
except Exception as e:
    print(f"It can be Error {e}")
else:
    print("Output :", b)
finally:
    print("Code is Executed when the program has an Error or has no Error\n")

#

try:
    number += 10
except Exception as e:
    print(f"It can be Error {e}")
else:
    print("Output :", number)
finally:
    print("Code is Executed when the program has an Error or has no Error\n")


try:
    amount = int(input("Enter the amount: "))
    if amount<0:
        raise f"Enter Positive amount"
except Exception as e:
    print(f"Error occured: {e}")
else:
    print(f"No Errors \nYou can Withdraw")
finally:
    print("Executed".center(25,"-"))

#1

#m=input("Enter DOB : ").split("-")
#m=m[::-1]
#print('/'.join(m))

#date,month,year=input().split("-")
#print(f'{year}/{month}/{date}')

#3

#w=input()
#print(w.translate(str.maketrans('aeiou','*****')))

#4

#f=list(map(float,input().split()))
#print(sum(f))
#print(max(f))


#5

#credentials = ("admin", "python123")
#username=input()
#password=input()
#if credentials[0]==username and credentials[1]==password:
#    print("Login successful")
#else:
#    print("Access deined")

#6

#names=set(input().split(","))
#print(sorted(names))

#7

#n=int(input())
#d={}
#max_marks=0
#res_name=' '
#for i in range(n):
#    name,marks=input().split()
#    marks=int(marks)
#    d[name]=marks
#    if marks>max_marks:
#        max_marks=marks
#        res_name=name
#
#print(d)
#print(res_name)
#print(max(d))
#print(max(d,key=d.get))


#8

#s=input().split()
#for i in s:
#    print(i[::-1],end=" ")

#9
#n=list(map(int,input().split()))
#while (0 in n):
#    n.remove(0)
#print(n)


#n=list(map(int,input().split()))
#li=[]
#for i in n:
#    if i!=0:
#        li.append(i)
#print(li)


#10

#s=input()
#d={}
#for i in s:
#    if i not in d and i!=" ":
#        d[i]=s.count(i)
#
#print(d)



# ---------------Weekly Test - numpies,pandas -----------------
'''
#1
num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

try:
    print(num / den)
except Exception as e:
    print("Cannot divide by zero!")


#2
num = list(map(int,input("Enter numbers: ").split()))
index = int(input("Enter the index number: "))
try:
    print(num[index])
except Exception as e:
    print(f"Index out of range {e}")


#3
import re
num = input("Enter the Mobile number: ")
check_num = re.fullmatch(r'^[6-9]{1}+\d{9}$',num)
#check_num = re.fullmatch(r'^(?:\+91|0)?[6-9]\d{9}$',num)
print(check_num.group() if check_num else "No Pattern")


print("\n\n\n\n\n\n")
# 7
import pandas as pd
data = {
    "Name" : ["John", "Alice", "Bob"],
    "Marks" : [75, 90, 85]
}

df_data = pd.DataFrame(data)
#print(df_data)
#for i in df_data:
#    if int(i["Marks"])> 80:
#        print(i["Name"])
result = df_data[df_data["Marks"] > 80]["Name"]
print(result)


print("\n\n\n\n\n\n\n\n")
# 9
import numpy as np
a=list(map(int,input("Enter numbers: ").split()))
b=list(map(int,input("Enter numbers: ").split()))
c=list(map(int,input("Enter numbers: ").split()))
d=list(map(int,input("Enter numbers: ").split()))

arr = np.array([a,b])
arr1 = np.array([c,d])
result = np.dot(arr, arr1)
print(result)

# 8
print("\n\n\n\n\n\n\n\n")
import numpy as np
import random
arr = np.random.randint(1,101,(10))
print(arr)
print("Mean: ", arr.mean())
print("Median: ", np.median(arr))
print("Standard Deviation: ", np.std(arr))

'''
# 10
import matplotlib.pyplot as plt
months = list(map(str, input("Enter names of the months: ").split()))
sales = list(map(int,input("Enter Sales: ").split()))
if len(months) == len(sales):
    plt.bar(months, sales)
    plt.title("Monthly Sales Data")
    plt.xlabel("Months")
    plt.ylabel("Sales")
    plt.show()

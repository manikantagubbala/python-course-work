#6.Lists.py

#Creating Lists
print("............Creating Lists.............")
l=[]
l=[1,2,3,4,5]
print(l)
print(list())
l.append('apple')
print(l)

#List with Nested Lists
print("...........List with Nested Lists..........")
l=[[1,2,3], {4,5,6}, (7,8,9), True, [1,'apple']]
print(l)
print(list("Python"))
list_from_tuple = list((1, 2, 3))
print(list_from_tuple)

#Accessing Elements in a List
print("........Accessing Elements in a List.........")
fruits=["banana",'apple','orange',"pineapple","watermelon","kiwi"]
print("Indexing[] : ", fruits[0])
print("Indexing[] : ", fruits[1])
print("Indexing[] : ", fruits[2])
print("Indexing[] : ", fruits[3])
print("Indexing[] : ", fruits[4])
print("Indexing[] : ", fruits[5])

print("Neg-Indexing[] : ", fruits[-1])
print("Neg-Indexing[] : ", fruits[-2])
print("Neg-Indexing[] : ", fruits[-3])
print("Neg-Indexing[] : ", fruits[-4])
print("Neg-Indexing[] : ", fruits[-5])
print("Neg-Indexing[] : ", fruits[-6])

print("Slicing[0] : ", fruits[0:3])
print("Slicing[1] : ", fruits[0:7:2])
print("Slicing[2] : ", fruits[1:7:2])
print("Slicing[3] : ", fruits[-3:])
print("Slicing[4] : ", fruits[::-1])
print("Slicing[5] : ", fruits[::-2])

f=fruits[1:7:2]
print("Slicing[6] : ", f[::-1])
print(fruits)
print(f)







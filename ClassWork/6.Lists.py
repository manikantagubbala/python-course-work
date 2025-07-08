#6.Lists.py

#6.1.Creating Lists
print("............Creating Lists.............")
l=[]
l=[1,2,3,4,5]
print(l)
print(list())
l.append('apple')
print(l)

#6.2.List with Nested Lists
print("...........List with Nested Lists..........")
l=[[1,2,3], {4,5,6}, (7,8,9), True, [1,'apple']]
print(l)
print(list("Python"))
list_from_tuple = list((1, 2, 3))
print(list_from_tuple)

#6.3.Accessing Elements in a List
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

#6.4.Adding Elements

g=list("Python Programming Language")
print("...........Adding Elements.......")
print(len(g))
print("Append() : ", fruits.append("cherry"))
print(fruits)
print("Insert() : ", fruits.insert(4,"mango"))
print(fruits)
print("Extend() : ", fruits.extend(["custard apple","guava"]))
print(fruits)

#6.5.Removing Elements

print("......Removing Elements........")
print("remove() : ", fruits.remove("kiwi"))
print(fruits)
print("pop() : ", fruits.pop(3))
print(fruits)
print("pop() : ", fruits.pop())
print(fruits)
#print("clear() : ", fruits.clear())
print(fruits)
del fruits[0]
print(fruits)
#del fruits
#print(fruits)

print("            ")
print("            ")
fruits.extend(["mango", "mango", "mango"])
print("count() : ", fruits.count("mango"))
print(fruits)
fruits.pop()
print(fruits)
print("count() : ", fruits.count("mango"))
print("reverse() : ", fruits.reverse())
print(fruits)

m=list("mani")
print(m[::-1])
print(m.reverse())
print(m)


fruit=fruits.copy()                       #shallow copy
print("fruits : ", fruits)                #fruits :  ['mango', 'mango', 'custard apple', 'cherry', 'watermelon', 'mango', 'orange', 'apple']
print("copy() : ", fruit)                 #copy() :  ['mango', 'mango', 'custard apple', 'cherry', 'watermelon', 'mango', 'orange', 'apple']
fruit.append("kiwi")
print("fruit : ", fruit)               # fruit :  ['mango', 'mango', 'custard apple', 'cherry', 'watermelon', 'mango', 'orange', 'apple', 'kiwi']
print("fruits : ", fruits)             # fruits :  ['mango', 'mango', 'custard apple', 'cherry', 'watermelon', 'mango', 'orange', 'apple']

fr=fruits                       #deep copy
fr.append("oranges")
print("fr : ", fr)                  #fr :  ['mango', 'mango', 'custard apple', 'cherry', 'watermelon', 'mango', 'orange', 'apple', 'oranges']
print("fruits : ", fruits)          #fruits :  ['mango', 'mango', 'custard apple', 'cherry', 'watermelon', 'mango', 'orange', 'apple', 'oranges']

print("any() : ", any(fruits))
print("all() : ", all(fruits))
fruits.sort()                                       #it can change from acen to dec order
print("sort() : ", fruits)                  #sort() :  ['apple', 'cherry', 'custard apple', 'mango', 'mango', 'mango', 'orange', 'oranges', 'watermelon']
sorted(fruits)                                      #doesn't change original value
print("sorted() : ", fruits)                #sorted() :  ['apple', 'cherry', 'custard apple', 'mango', 'mango', 'mango', 'orange', 'oranges', 'watermelon']
print("max() : ", max(fruits))
print("min() : ", min(fruits))
fruits.append(0)
print("fruits : ", fruits)              #fruits :  ['apple', 'cherry', 'custard apple', 'mango', 'mango', 'mango', 'orange', 'oranges', 'watermelon', 0]
print("all() : ", all(fruits))          #all() :  False

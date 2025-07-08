#8.sets.py
print("....creating sets.......")
s=set()
print("sets{} : ", s)
s={1,2,3,4,5,1,2,1,54,0,28,5,1,5,7,9,8}
print("sets{} : ", s)

# false=0, true=1
cls={'bhaskar', True, 'raju', 'vijay', 'teja', 'mahesh',1,3.4 }
clz={'aditya', 'eswar', 'raju', 0, 'vijay', 'venky', False, (1,2,3,4)}
print("class : ", cls, "college : ", clz)

t=(True,1,34.4,'mani')
print(t)
l=[True,1,34.4,'mani']
print(l)

print("....operations on sets.......")
m={1,4,72,81,54,64,91}
print("sets{} : ", s)
print("sets{} : ", m)
print("Membership(1) : ", 1 not in s)
print("Membership(2) : ", 11 not in s)
print("Membership(3) : ", 81  in m)
print("Membership(4) : ", 11 not in m)
print("union : ", s | m)
print("Union : ", s.union(m))





print("......Built in functions......")
print("sets{} : ", m)
print("length : ",len(m))   
print("sorted : ", sorted(m))
print("max : ", max(m))      
print("min : ", min(m))   
print("sum : ", sum(m))

print("sets{} : ", s)  
print("length : ",len(s))
print("sorted : ", sorted(s))
print("max : ", max(s))      
print("min : ", min(s))   
print("sum : ", sum(s))

i=[1,2,3,'iu', False, 5+7j]
print("sets{list to set} : ", set(i))

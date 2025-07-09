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
print("sets{} : ", s)                                   #sets{} :  {0, 1, 2, 3, 4, 5, 7, 8, 9, 54, 28}
print("sets{} : ", m)                                   #sets{} :  {64, 1, 81, 4, 54, 72, 91}
print("Membership(1) : ", 1 not in s)                   #Membership(1) :  False
print("Membership(2) : ", 11 not in s)                  #Membership(2) :  True
print("Membership(3) : ", 81  in m)                     #Membership(3) :  True
print("Membership(4) : ", 11 not in m)                  #Membership(4) :  True
print("union : ", s | m)                                #union :  {0, 1, 2, 3, 4, 5, 64, 7, 8, 9, 72, 81, 54, 91, 28}
print("Union : ", s.union(m))                           #Union :  {0, 1, 2, 3, 4, 5, 64, 7, 8, 9, 72, 81, 54, 91, 28}
print("Intersection : ", s & m)
print("Intersection : ", s.intersection(m))
print("Difference : ", s - m)
print("Difference : ", s.difference(m))
print("symmetric : ", s ^ m)
print("symmetric : ", s.symmetric_difference(m))
m.update({3,98})
print(m)
s.intersection_update(m)
print(s)
print(m)
print("Intersection : ", m & s)

print("sets{s} : ", s) 
print("sets{m} : ", m) 
s={1,3,5,2,9,7,6,99,89,100109}
m={2,6,7,9,1,3}
print(s)
print(m)
print("Subset: ", s.issubset(m))
print("Subset: ", s <= m)
print("Superset : ", s.issuperset(m))
print("Superset : ", s >= m)


s={1,2,3,4}
m={1,5,6,7,8,9}
print("sets{s} : ", s)
s.update(m)
print("update : ", s)               #update :  {1, 2, 3, 5, 6, 7, 9, 100109, 89, 99}

print(m | s)                                 # {1, 2, 3, 5, 6, 7, 9, 100109, 89, 99}
print("sets{s} : ", s)
print("sets{m} : ", m)


s={1,2,3,4,7}
m={1,5,6,7,8,89}
print(s & m)
print("sets{s} : ", s)

s.intersection_update(m)
print("intersection_update(s) : ", s)
print(m)

s={1,2,3,4,7}
m={1,5,6,7,8,89}
print(s - m)
print(s)                            #s={1,2,3,4,7}

s.difference_update(m)
print("difference_update(s) : ", s)  #{2, 3, 4}






#print("......Built in functions......")
#print("sets{} : ", m)
#print("length : ",len(m))   
#print("sorted : ", sorted(m))
#print("max : ", max(m))      
#print("min : ", min(m))   
#print("sum : ", sum(m))
#
#print("sets{} : ", s)  
#print("length : ",len(s))
#print("sorted : ", sorted(s))
#print("max : ", max(s))      
#print("min : ", min(s))   
#print("sum : ", sum(s))
#
#i=[1,2,3,'iu', False, 5+7j]
#print("sets{list to set} : ", set(i))


#frozen = frozenset([1, 2, 3])
#print(frozen)
#
#l=[1,23,4]
#print(set(l))
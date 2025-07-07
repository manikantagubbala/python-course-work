#7.1.Tuple.py

t1=()
tu=(1,)
tup=176,23,3,14
t=(1,2,3,4,"manikanta","eswar","aditya","venky",69.9)
print(tuple())
print("Empty tuple() : ", t1)
print("single tuple() : ", tu)
print("Without () : ", tup)
print( "tuple() : ", t)

#Accessing Tuple Elements
print("")
print("........Accessing Tuple Elements......")
print("Indexing[] : ", t[2])
print("Indexing[] : ", t[-2])
print("slicing[1] : ", t[::-1])
print("slicing[2] : ", t[0:9:2])
print("slicing[3] : ", t[1:8:2])
print("slicing[4] : ", t[4:])
print("slicing[5] : ", t[:4])
print("slicing[6] : ", t[-5:])


#Operations on Tuples
print("")
print("......Operations on Tuples.......")
print("Concatenation : ", tup + t)
print("Repeatition : ", tup*5)
print("Repeatition : ", t[5:]*5)
print("Membership : ", "venky" in t)
print("Membership : ", "manikanta" not in t)
print("Membership : ", "venky" in tup)
print("Membership : ", "manikanta" not in tup)

num = (1,2,3,4,5)                           #packing
(a,b,c,d,e) = num                           #unpacking
print(c)        
print(d)        
print(e)
print(a)
print(b)

c=tup + t
print("tuple() : ", c)
print("count() : ", c.count(2))
print("Index() : ", t.index("eswar"))
print("Index() : ", t.index(69.9))
print("length : ",len(t)) 
print("sorted : ", sorted(tup))
print("max : ", max(tup))   
print("min : ", min(tup)) 
m=t[4:8]  
print(sorted(m))
print("Sum() : ", sum(tup))

print("")
mt=(1,2.4,'nani',"mani",[1,2,4],('sai','krishna','chaitanya'))
print("nested tuple : ", mt[4].append(998))
mt[4][0]="surya"
print("tuple() : ", mt)

li=[2,5,7,9.5,67,43.43,345,6]
print(type(li))
print("tuple() : ", tuple(li))









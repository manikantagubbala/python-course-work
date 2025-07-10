#9.TypeConversion.py
print(".....Integer.......")
i=10
print(float(i))
print(complex(i))
print(str(i))
print(bool(i))
#print(list(i))             #It can't covert int to list
#print(tuple(i))            #It can't covert int to tuple
#print(set(i))              #It can't covert int to set
#print(dict(i))             #It can't covert int to dictionary

print("")
print(".....float.......")
f=10.9
print(int(f))
print(complex(f))
print(str(f))
print(bool(f))
#print(list(f))             #It can't covert float to list
#print(tuple(f))            #It can't covert float to tuple
#print(set(f))              #It can't covert float to set
#print(dict(f))             #It can't covert float to dictionary

print("")
print(".....Complex.......")
c=10+5j
#print(float(c))
#print(int(c))
print(str(c))
print(bool(c))
#print(list(c))             #It can't covert complex to list
#print(tuple(c))            #It can't covert complex to tuple
#print(set(c))              #It can't covert complex to set
#print(dict(c))             #It can't covert complex to dictionary

print("")
print("boolean".center(20,'.'))
b=True
print(int(b))
print(float(b))
print(complex(b))
print(str(b))
#print(list(b))
#print(tuple(b))
#print(set(b))
#print(dict(b))

print("")
print("string".center(20,'.'))
s='manikanta'
#print(int(s))
#print(float(s))
s='20.9'
print(float(s))
s='20'
print(int(s))
#print(complex(s))
print(bool(s))
print(list(s))
print(tuple(s))
print(set(s))
#print(dict(s))

print("")
print("list".center(20,'.'))
l=[1,2,3,4,'nani']
#print(int(l))
#print(float(l))
#print(complex(l))
print(bool(l))
print(str(l))
print(tuple(l))
print(set(l))
#print(dict(l))
l=[(1,3.4),(2,4)]
print(dict(l))

print("")
print("tuple".center(20,'.'))
t=(1,2,3,4,'nani')
#print(int(t))
#print(float(t))
#rint(complex(t))
print(bool(t))
print(str(t))
print(list(t))
print(set(t))
#print(dict(t))
t=((1,2),('name','lilly'))
print(dict(t))

print("")
print("set".center(20,'.'))
a={1,2,3,4,'nani'}
#print(int(a))
#print(float(a))
#print(complex(a))
print(bool(a))
print(str(a))
print(tuple(a))
print(list(a))
#print(dict(a))
s={(1,2),('name','lilly')}
print(dict(t))

print("")
print("dictionary".center(20,'.'))
d={1:'mani', 2:'aditya', 3:'eswar'}
#print(int(d))
#print(float(d))
#print(complex(d))
print(bool(d))
print(str(d))
print(tuple(d))
print(set(d))
print(list(d))









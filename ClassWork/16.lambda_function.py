print()

'''
var = lambda args: statements
var()
'''

s=sorted([(2,3),(4,1),(8,2)], key= lambda i:i[-1])
print(s)

l=['Manikanta','Aditya','Kiran','nani']
m=sorted(l,key= lambda i:i[0],reverse=True)
print(m)

#filter()
l=[1,2,3,43,45,98]
f=list(filter(lambda i : i%2==0, l))
print(f)

l=[0,0,0,0,0,0,0,5,0,67,4,4,5,56666666,0,0,0,5,65,56,7]
f=tuple(filter(lambda i: i!=0, l))
print("Using Tuple: ",f)

s='python'
st=list(map(lambda i:i, s))
print(len(st))


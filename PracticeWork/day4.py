a={1,2,3,4,5}
#print(a)
a.update({8,9})
b={10,11,12,30,40,5}
b.update({1,2})
print(a)
print(b)
a.intersection_update(b)
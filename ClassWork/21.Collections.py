#Collections.py

import collections

'''
word = "Hello python program"
d=collections.Counter(word)
print(d)


num = (1,2,3,4,5,1,23,34,5,2,1,3,4,5,3)
n=collections.Counter(num)                      #It gives nums and their count
print("Nums as dict: ", n)                      #Nums as dict:  Counter({1: 3, 3: 3, 5: 3, 2: 2, 4: 2, 23: 1, 34: 1})


names = ('mani', 'eswar', 'aditya', 'venky', 'sai')
name = collections.Counter(names)
print(name)                                     #Counter({'mani': 1, 'eswar': 1, 'aditya': 1, 'venky': 1, 'sai': 1})

'''
#default dictnary

course = "Python Program"
d={}
for i in course:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
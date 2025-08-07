#Collections.py
import collections
from collections import deque
import itertools


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


course = "Python Program"
d={}
for i in course:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

'''

#default dictnary

#s="Python Program"
#d=collections.defaultdict(int)
#for i in s:
#    d[i] += 1
#print(d)

#word = "abcde"
#d=collections.defaultdict(str)
#for i in range(1,len(word)+1):
#    d[i]+= word[i-1]
#print(d)

#a=[1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
#d=collections.defaultdict(str)
#for i in a:
#    d[i] += "s "
#print(d)


#a=[1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
#d=collections.defaultdict(float)
#for i in a:
#    d[i] += 1
#print(d)

'''

print("----------Deque------------")

#Stacks and Queues

print("1.Stack".center(20,"-"))
stack = deque()

stack.appendleft(1)
stack.appendleft(2)
stack.appendleft(3)
stack.popleft()
stack.appendleft(4)
stack.popleft()
stack.appendleft(5)
stack.appendleft(6)

print("bike_park_in_cinemahall: ",stack)

print("-------------2.Queue----------")
queue = deque()

queue.appendleft("c1")
queue.appendleft("c2")
queue.appendleft("c3")
queue.pop()
queue.appendleft("c4")
queue.pop()
queue.appendleft("c5")
queue.appendleft("c6")
queue.pop()
queue.appendleft("c7")
queue.appendleft("c8")
queue.pop()
queue.appendleft("c9")

print("Ca_park: ",queue)

'''

#Itertools ==> combinations and Permutations
#Combination of "abc",2  ==> ab ac bc
#Permutations of "abc"2  ==> ab ac ba bc ca cb

print(tuple(itertools.combinations("abc",2)))
print(tuple(itertools.permutations("abc",2)))
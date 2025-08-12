print()
'''
def show(l):
    for i in l:
        st,end=i.split("..")
        reelsOf_i=[i for i in range(int(st),int(end)+1)]
        yield reelsOf_i

reels=['1..100','101..200','201..300','301..400','401..500']
nextfeed=show(reels)

while True:
    scroll=input("[c]ontinue / [e]xit: ")
    if scroll=='c':
        print(next(nextfeed))
    else:
        break
'''

'''
def even_odd(n):
    if n%2==0:
        yield True
    else:
        yield False
n=int(input())
print(next(even_odd(n)))
'''
def even_odd_list(numbers):
    for n in numbers:
        yield n % 2 == 0

nums = [2, 3, 4, 5]
for result in even_odd_list(nums):
    print(result)

#

def even(n):
    yield n%2==0
n=7
print("\n",next(even(n)))
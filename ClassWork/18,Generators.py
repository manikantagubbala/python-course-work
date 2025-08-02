print()
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

#def num(a):
#    yield a+2
#print(next(num(5)))
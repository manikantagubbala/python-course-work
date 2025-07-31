print()
def show(a):
    for i in a:
        st,en=i.split("to")
        yield i

reels=['1to100','101to200','301to400','401to500']
n=show(reels)
#print(next(n))

while True:
    scroll_exit=input("Enter any ")
    if scroll_exit=='c':
        print(next(n))
    else:
        break
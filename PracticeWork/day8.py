
#i=input("Enter ").lower()

#i=i.replace("a",'*')
#i=i.replace("e",'*')
#i=i.replace("i",'*')
#i=i.replace("o",'*')
#i=i.replace("u",'*')

#i=i.translate(str.maketrans('aeiou','*****'))
#print(i)


#i=input("Enter : ").split()
#i=i[0][::-1]
#print(i)


n=list(map(int,input("Enter : ").split()))

for i in n:
    if 0 in i:
        n.remove(0)
        print(n)



#d=eval(input("Enter : "))
#print(max(d,key=d.get))

#k=input("Enter : ").split(",")
#k=set(k)
#print(sorted(k))


#n=int(input("Enter number : "))
#for i in n:
#    m=n*(i-1)
#    print(m)

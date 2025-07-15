'''i=input("Enter ")

i=i.replace("a",'*')
i=i.replace("e",'*')
i=i.replace("i",'*')
i=i.replace("o",'*')
i=i.replace("u",'*')
#i.translate(str.maketrans('aeiou','*****'))
#i=i.replace('a','*')
print(i)

'''

i=input("Enter : ").split()
n=0
for b in i:
    print(i[n][::-1], end=" ")
    n+=1

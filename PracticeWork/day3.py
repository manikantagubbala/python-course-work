fname="suryaprakasharao"
print(len(fname))                                   #16
print("Slicing- var[] : ", fname[:16])              #Slicing- var[] :  suryaprakasharao
print("Slicing- var[] : ", fname[:])                #Slicing- var[] :  suryaprakasharao
print("Slicing- var[] : ", fname)                   #Slicing- var[] :  suryaprakasharao
print("Slicing- var[] : ", fname[5:16])             #Slicing- var[] :  prakasharao
print("Slicing- var[] : ", fname[1:16:2])           #Slicing- var[] :  uypaahro
print("Slicing- var[] : ", fname[0:16:2])           #Slicing- var[] :  srarksaa
print("Slicing- var[] : ", fname[0:16:4])           #Slicing- var[] :  saka
print("Slicing- var[] : ", fname[1:16:3])           #Slicing- var[] :  uaasr
print("Slicing- var[] : ", fname[1:16:5])           #Slicing- var[] :  urh

a='HackerRank.com presents "Pythonist 2" '
print(a.swapcase())

b='this is a string'
c=b.split(" ")
print("-".join(c))
print(c)

fname="Ross"
lname="Taylor"
s="Hello first last ! You just delved into python."

d="abracadabra"
#print(d[:4] + "k" + d[5:])
#print(d)
e=list(d)
e[4]
s=" ".join(e)
print(s)
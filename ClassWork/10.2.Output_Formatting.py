#10.2.Output_Formatting.py

i=16
s='Manikanta'
f=11.2

print(i,s,f)
print("Num:",i, 'Name:',s, 'DOb:',f)
print("Num: ",i, '\nName:',s, '\nDOb:',f)
print("Num:%d \nName:%s \nDOb:%2f" %(i, s, f))

print(" ")
print("f s t r i n g".center(75," "))
print(f'Hello, I am {s}. I am {i} years old')

print("formatting".center(25," "))
print("i am {}. {} years old".format(s,i))
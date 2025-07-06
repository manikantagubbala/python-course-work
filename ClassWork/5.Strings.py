#5.Strings.py
#5.1.OperationsOnStrings

print("......OperationsOnStrings.......")
s1='bhuvana '
s2='Manikanta'
print("Concatenation(+) : ", s1 + s2)             # Concatenation(+) :  bhuvana Manikanta
print("Repetition(*) : ", s1*4)                   # Repetition(*) :  bhuvana bhuvana bhuvana bhuvana 
print("Repetition(*) : ", s2*4)                   # Repetition(*) :  ManikantaManikantaManikantaManikanta
print("Indexing : ", s1[0])                       # Indexing :  b
print("Indexing : ", s1[1])                       # Indexing :  h
print("Indexing : ", s1[2])                       # Indexing :  u
print("Indexing : ", s1[3])                       # Indexing :  v
print("Indexing : ", s1[4])                       # Indexing :  a
print("Indexing : ", s1[5])                       # Indexing :  n
print("Indexing : ", s1[6])                       # Indexing :  a
print("Indexing : ", s1[7])                       # Indexing :   

s="IamManikantaIcompleted BTech in 2025 at KIET"
print("Membership : ", "completed" in s)               # Membership :  True
print("Membership : ", "2025" in s)                    # Membership :  True
print("Membership : ", "mani" not in s)                # Membership :  True
print("Membership : ", "bhuvana" in s)                 # Membership :  False

fname="suryaprakasharao"
print(len(fname))
print("Slicing- var[] : ", fname[:])

#5.2.Built-in String Functions
#1. len() - Returns the length of the string.
#2. max() / min() - Returns the maximum or minimum character (based on ASCII values).
#3. sorted() - Returns a sorted list of characters.
#4. chr() / ord() - Converts between characters and their ASCII codes

print("........Built-in String Functions..........")
m='Looking beautiful'
print("length : ",len(m))           #length :  17
print("max : ", max(m))             #max :  u
print("min : ", min(m))             #min :   
print("sorted : ", sorted(m))       #sorted :  [' ', 'L', 'a', 'b', 'e', 'f', 'g', 'i', 'i', 'k', 'l', 'n', 'o', 'o', 't', 'u', 'u']
print("character : ", chr(97))      #character :  a
print("Order : ", ord(' '))         #Order :  32


#5.3.Case Conversion Methods
#1.upper()
#2.lower()
#3.capitalize()
#4.title()
#5.swapcase()
#6.casefold()

print(".........Case Conversion Methods.........")
c='''i can improve mY SELF'''
print("upper('A') : ", c.upper())                  #upper() :  I CAN IMPROVE MY SELF
print("lower('a') : ", c.lower())                  #lower() :  i can improve my self
print("capitalize(Ab cd) : ", c.capitalize())      #capitalize() :  I can improve my self
print("title(Ab Cd) : ", c.title())                #title() :  I Can Improve My Self
print("swapcase(A-a, a-A) : ", c.swapcase())       #swapcase() :  I CAN IMPROVE My self


#5.4.Search & Find Methods
print("...........Search & Find Methods..............")
f="adityaMandala"
print("find : ", f.find('a'))           #find :  0
print("rfind : ", f.rfind('a'))         #rfind :  12
print("find : ", f.find('x'))           #find :  -1
#print("index : ", f.index('x'))        #error
print("index : ", f.index('d'))         #index :  1
print("rindex : ", f.rindex('d'))       #rindex :  9
print("count : ", f.count('a'))         #count : 5


#5.5.Alignment & Formatting Methods

print(".....Alignment & Formatting Methods......")
print("center : ", f.center(20,"*"))         #center :  ***adityaMandala****
print("ljust : ", f.ljust(16,"*"))           #ljust :  adityaMandala***
print("rjust : ", f.rjust(16,"*"))           #rjust :  ***adityaMandala
print("zfill : ", f.zfill(16))               #zfill :  000adityaMandala
print("zfill : ", '8978411298'.zfill(16))    #zfill :  0000008978411298


#5.6.String Testing Methods (Boolean Results)

print("..............String Testing Methods (Boolean Results).........")
g='Manikanta12324'
print("startswith(sub) : ", f.startswith('d'))          #startswith(sub) :  False
print("startswith(sub) : ", f.startswith('a'))          #startswith(sub) :  True
print("endswith(sub) : ", f.endswith('d'))              #endswith(sub) :  False
print("endswith(sub) : ", f.endswith('a'))              #endswith(sub) :  True
print("isspace : ", f.isspace())                        #isspace :  False
print("isalpha : ", f.isalpha())                        #isalpha :  True
print("isalpha : ", g.isalpha())                        #isalpha :  False
print("isalnum : ", g.isalnum())                        #isalnum :  True
print("isupper : ", f.isupper())                        #isupper :  False
print("islower : ", f.islower())                        #islower :  False
print("istitle : ", f.istitle())                        #istitle :  False
print("isidentifier : ", f.isidentifier())              #isidentifier :  True
print("istitle : ", g.istitle())                        #istitle :  True

print("................")
print("         isdecimal()  ")
print("isdecimal() : ", '123'.isdecimal())            #isdecimal() :  True
print("isdecimal() : ", '123.67'.isdecimal())         #isdecimal() :  False
print("isdecimal() : ", '12abc3'.isdecimal())         #isdecimal() :  False
print("isdecimal() : ", 'Ⅷ'.isdecimal())            #isdecimal() :  False
print("isdecimal() : ", '٣'.isdecimal())              #isdecimal() :  True
print("isdecimal() : ", '²'.isdecimal())              #isdecimal() :  False
print("isdecimal() : ", '⅓'.isdecimal())              #isdecimal() :  False
print("isdecimal() : ", '五'.isdecimal())             #isdecimal() :  False

print("................")
print("         isdigit()  ")
print("isdigit() : ", '123'.isdigit())              #isdigit() :  True
print("isdigit() : ", '123.67'.isdigit())           #isdigit() :  False
print("isdigit() : ", '12abc3'.isdigit())           #isdigit() :  False
print("isdigit() : ", 'Ⅷ'.isdigit())              #isdigit() :  False
print("isdigit() : ", '٣'.isdigit())                #isdigit() :  True
print("isdigit() : ", '²'.isdigit())                #isdigit() :  True
print("isdigit() : ", '⅓'.isdigit())                #isdigit() :  False
print("isdigit() : ", '五'.isdigit())               #isdigit() :  False

print("................")
print("         isnumeric()  ")
print("isnumeric() : ", '123'.isnumeric())          #isnumeric() :  True
print("isnumeric() : ", '123.67'.isnumeric())       #isnumeric() :  False
print("isnumeric() : ", '12abc3'.isnumeric())       #isnumeric() :  False
print("isnumeric() : ", 'Ⅷ'.isnumeric())          #isnumeric() :  True
print("isnumeric() : ", '٣'.isnumeric())            #isnumeric() :  True
print("isnumeric() : ", '²'.isnumeric())            #isnumeric() :  True
print("isnumeric() : ", '⅓'.isnumeric())            #isnumeric() :  True
print("isnumeric() : ", '五'.isnumeric())           #isnumeric() :  True

#5.7.Replace & Modify Methods

print(".................Replace & Modify Methods...........")

print("replace(old,new) : ", f.replace('a', '@'))                           #replace(old,new) :  @dity@M@nd@l@
print("replace(old,new) : ", f.replace('ad', '@%'))                         #replace(old,new) :  @%ityaMandala    it has to change substring                           
print("maketrans() : ", f.maketrans('a', '@'))                              #maketrans() :  {97: 64}
print(ord('a'))                                                             #97
print(ord('@'))                                                             #64
print("translate(table) : ", f.translate(str.maketrans('a', '@')))          #translate(table) :  @dity@M@nd@l@
print("translate(table) : ", f.translate(str.maketrans('ad', '@%')))        #translate(table) :  @%ity@M@n%@l@     it has to change c


#5.8.Whitespace & Trimming Methods
print("..........Whitespace & Trimming Methods.......")
m='   manikanta '
print("strip() :",m.strip())                            #strip() : manikanta
print("lstrip() :",m.lstrip())                          #lstrip() : manikanta 
print("rstrip() :",m.rstrip())                          #rstrip() :    manikanta

#5.9.Splitting & Joining Methods
#partition() and rpartition() both return a 3-part tuple.
m='manikanta bhuvana gubbala'
n='helloworld'
print("........Splitting & Joining Methods............")                           
print("split() : ", m.split())                                                     #split() :  ['manikanta', 'bhuvana', 'gubbala']
print("rsplit() : ", m.rsplit())                                                   #rsplit() :  ['manikanta', 'bhuvana', 'gubbala']
print("split() : ", m.split(" ",1))                                                #split() :  ['manikanta', 'bhuvana gubbala']
print("rsplit() : ", m.rsplit(" ",1))                                              #rsplit() :  ['manikanta bhuvana', 'gubbala']
print("splitlines() : ", "Hello\nworld\ni\nam\nManikanta".splitlines())            #splitlines() :  ['Hello', 'world', 'i', 'am', 'Manikanta']
print("join() : ", " ".join(m))                                                    #join() :  m a n i k a n t a   b h u v a n a   g u b b a l a
print("join() : ", " ".join(['manikanta',"bhuvana",'''gubbala''']))                #join() :  manikanta bhuvana gubbala
print(n[0:5]+" "+n[5:10])                                                          #hello world
print(n[1:10:2])                                                                   #elwrd
print("partition() : ", m.partition(" "))                                          #partition() :  ('manikanta', ' ', 'bhuvana gubbala')
print("rapartition() : ", m.rpartition(" "))                                       #rapartition() :  ('manikanta bhuvana', ' ', 'gubbala')
print("partition() : ", "hello hi mani aditya eswar".partition(" "))               #partition() :  ('hello', ' ', 'hi mani aditya eswar')


#5.10.Encoding & Decoding Methods
print("..........Encoding & Decoding Methods.........")

en="hello Hello नमते你好"
de=b' caf\xc3\xa9 \xf0\x9f\x99\x82'
print("Encode() : ", en.encode())
print("Decode() : ", de.decode())



#5.Strings.py
#5.1.OperationsOnStrings

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


#5.2.Built-in String Functions
#1. len() - Returns the length of the string.
#2. max() / min() - Returns the maximum or minimum character (based on ASCII values).
#3. sorted() - Returns a sorted list of characters.
#4. chr() / ord() - Converts between characters and their ASCII codes


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

c='''i can improve mY SELF'''
print("upper('A') : ", c.upper())                  #upper() :  I CAN IMPROVE MY SELF
print("lower('a') : ", c.lower())                  #lower() :  i can improve my self
print("capitalize(Ab cd) : ", c.capitalize())      #capitalize() :  I can improve my self
print("title(Ab Cd) : ", c.title())                #title() :  I Can Improve My Self
print("swapcase(A-a, a-A) : ", c.swapcase())       #swapcase() :  I CAN IMPROVE My self



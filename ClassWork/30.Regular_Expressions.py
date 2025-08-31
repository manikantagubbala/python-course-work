# 30.Regular_Expressions.py
import re

result = re.match('Hellooo',"Hello World")                          # match is nothing but Startswith
print(result.group() if result else "No Pattern")

match_with = re.match(r'[aeiouAEIOU]',"Apple")                      # 'r' -> rawString  
print(match_with.group() if match_with else "No Pattern")

match_with = re.match(r'[A-Z]',"Bike Car")
print(match_with.group() if match_with else "No Pattern")

match_with = re.match(r'\d{2}',"123Apple")                          # for check any int we use '\d'  and {2} -> startswith range {2}
print(match_with.group() if match_with else "No Pattern")

match_with = re.match(r'[a-z]+',"apple and Orange")                 # '+' -> it prints whole word
print(match_with.group() if match_with else "No Pattern")

# search
print("Search".center(20,"*"))
res = re.search(r'[0-9]{7}',"Mobile No- 8978411298")                # search is nothing but to find in a whole string
print(res.group() if res else "No Pattern")

# FindAll
print("FindAll".center(20,"*"))
find = re.findall(r'[0-9]{2}','Mani - 43, Aditya - 40, Eswar - 45') 
print(f'\nfindAll - {find}')                                        # ['4', '3', '4', '0', '4', '5']

findall_dot = re.findall(r'h..',"hat hit hot hot")                  # '.' --> default value
print(findall_dot)

findall_dot = re.findall(r'\w',"hat hit hot hot")                   # '\w' --> prints all words
print(findall_dot)

findall_dot = re.findall(r'\s',"hat hit hot hot")                   # '\s' --> prints all spaces
print(findall_dot)

findall_dot = re.findall(r'\S',"hat hit hot hot")                   # '\S' --> prints all words
print(findall_dot)

findall_dot = re.findall(r'\W',"hat hit hot hot")                   # '\W' --> prints all spaces
print(findall_dot)

# FIndIter
print("findIter".center(20,"-"))
find_iter = re.finditer(r'[0-9]{1,}','Mani - 43, Aditya - 40, Eswar - 45') # {1,} --> {stswith,endswith}
for i in find_iter:
    print(i.group(),i.start())                                       # start() --> it shows index

# FullMatch
print("fulMatch".center(20,"-"))
full_match = re.fullmatch(r'apple',"apple")
print(full_match.group() if full_match else "No Pattern")

full_match = re.fullmatch(r'(apple)*',"")                           # '*' no word, it prints empty space
print(full_match.group() if full_match else "No Pattern")

full_match = re.fullmatch(r'(apple)+',"")                           # '+' atleast one word
print(full_match.group() if full_match else "No Pattern")

full_match = re.fullmatch(r'\d{10}',"8978411298")                   
print(full_match.group() if full_match else "No Pattern")

full_match = re.fullmatch(r'^[6-9]\d{9}',"5978411298")              # '^' --> startswith, [6,9] -->[start,end]
print(full_match.group() if full_match else "No Pattern")

full_match = re.fullmatch(r'M...',"M@ni")
print(full_match.group() if full_match else "No Pattern")


# split
print("Split".center(20,"-"))
split_words = re.split(r'[,:.@]',"bmanikanta1357@gmail.com,manikanta:bhuvana")  # split with multiple characters
print(split_words)

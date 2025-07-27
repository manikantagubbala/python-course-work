print()
chat={
    'Alice': 'Good morning!',
    'Bob': 'Morning Alice!',
    'Charlie': 'Morning everyone!',
    'Alice': 'Hope you all have a great day.',
    'Bob':' You too, Alice!',
    'Charlie': "Let's plan something fun this weekend"
}

print(chat)
print(set(chat.keys()))
print(len(chat.values()))

v=[]
for i in chat['Bob'].split():
    v.append(i)
print("length: ",len(v))

c={
    'Alice': [(' Good morning!', 0), (' Hope you all have a great day.', 3)], 
     'Bob': [(' Morning Alice!', 1), (' You too, Alice!', 4)],
    'Charlie': [(' Morning everyone!', 2), (" Let's plan something fun this weekend.", 5)]
    }


#print("Total no.of words: ")
#l=c['Alice'][1][0].split() + c['Alice'][0][0].split()
#print(len(l))
#print()
total=0
for i in c:
    l=c[i][1][0].split() + c[i][0][0].split()
    total+=len(l)
print(total)
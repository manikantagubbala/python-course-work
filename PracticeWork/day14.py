data={
    'mani':98,
    'aditya':88,
    'eswar':78,
    'venky':68,
    'krishna':60
}
print(data)
print(data.keys())
print(data.values())
print(data.items())
print(len(data))
data['sai']=75
print(data)
print(len(data))
data['aditya']=data['aditya']+10
print(data)
print(data.get('mani'))
print(data.get('balu'))
print(data)
print(len(data))
print(data.setdefault('balu',100))
print(data)
print(len(data))

data.popitem()
print(data)
data.pop('mani')
print(data)
sorted(data)
print(data)



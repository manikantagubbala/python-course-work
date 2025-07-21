'''
print("Bill StatementL:".center(30," "))
data={
    1:{'name':'Rice','price':60},
    2:{'name':'Sambar Rice','price':50},
    3:{'name':'Mutton Biryani','price':199},
    4:{'name':'Chicken Biryani','price':99},
    5:{'name':'Chicken curry','price':80},
    6:{'name':'Mutton Curry','price':120},
    7:{'name':'Omlet','price':35}
}


for i in data:
    print(f'{i}.{data[i]['name']} - Rs.{data[i]['price']}')

items=list(map(int,input("Enter your Items(1 2 3 4):").split()))

print("Your Bill".center(30,"*"))
total=0
s=set()

for i in items:
    if i not in s:
        c=items.count(i)
        print(f'{data[i]['name']} - {c} * {data[i]['price']} = {c*data[i]['price']}')
        total+=data[i]['price'] * c
        s.add(i)
print("Total Bill Amount: ",total)



data={
    'Biryani':99,
    'Omlet':35,
    'Mutton Biryani':199,
    'Chicken curry':80

}

total=0
while True:
    Item_Name=input("Enter your Items: ").capitalize()
    if Item_Name=='0':
        break
    quantity=int(input("Enter Quantity: "))
    total+=data[Item_Name]*quantity

print("Total Bill Amount: Rs.",total)
print("Thank You Visit again".center(50,"*"))

'''
'''
print("Photo Gallery:".center(20," "))
p={
    1:{'photo':'beach','.for':'.png'},
    2:{'photo':'mountain','.for':'.jpg'},
    3:{'photo':'party1','.for':'.jpg'},
    4:{'photo':'selfie','.for':'.png'},
    5:{'photo':'birthday','.for':'.png'},
    6:{'photo':'concert','.for':'.jpg'},
    7:{'photo':'sunset','.for':'.png'},
    8:{'photo':'trip1','.for':'.jpg'},
}

for i in p:
    print(f'{i}. {p[i]['photo']}{p[i]['.for']}')

photos=list(map(int,input("Enter your photo(1 2 3 4): ").split()))
s=set()
print("Sharing the following photos: ")
for i in photos:
    if i not in s:
        print(f'{p[i]['photo']}{p[i]['.for']}')
        s.add(i)
'''

p={
    'img1':'beach.png',
    'img2':'mouintain.jpg',
    'img3':'party1.png',
    'img4':'selfie.jpg',
    'img5':'trip1.png',
    'img6':'sunset.jpg',
    'img7':'sunrise.png',
    'img8':'birthday.jpg',

}

s=set()
while True:
    photo=input("Enter your img: ").lower()
    if photo=='0':
        break
    s.add(photo)

s=str(s)
print(s)
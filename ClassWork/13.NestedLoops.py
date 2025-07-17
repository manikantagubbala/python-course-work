#13.NestedLoops.py
print("'*' Pattern".center(25," "))
for row in range(5):
    for col in range(5):
        print(row, end=' ')
    print()

print()

for row in range(5):
    for col in range(5):
        print(col, end=' ')
    print()

print()

for row in range(5):
    for col in range(row+1):
        print(row,end=" ")
    print()

print()

for row in range(5):
    for col in range(5-row):
        print(row,end=" ")
    print()






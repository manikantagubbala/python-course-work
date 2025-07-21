#13.NestedLoops.py
print("'*' Pattern".center(25," "))
for row in range(5):                                #   0 0 0 0 0 
    for col in range(5):                            #   1 1 1 1 1
        print(row, end=' ')                         #   2 2 2 2 2  
    print()                                         #   3 3 3 3 3  
                                                    #   4 4 4 4 4  
print("2".center(15," "))

for row in range(5):                                #   0 1 2 3 4
    for col in range(5):                            #   0 1 2 3 4
        print(col, end=' ')                         #   0 1 2 3 4
    print()                                         #   0 1 2 3 4
                                                    #   0 1 2 3 4    
print("3".center(15," "))

for row in range(5):                                #   0
    for col in range(row+1):                        #   1 1
        print(row,end=" ")                          #   2 2 2
    print()                                         #   3 3 3 3
                                                    #   4 4 4 4 4
print("4".center(15," "))

for row in range(5):                                #   0 0 0 0 0
    for col in range(5-row):                        #   1 1 1 1
        print(row,end=" ")                          #   2 2 2
    print()                                         #   3 3
                                                    #   4
print("5".center(15," "))

for i in range(5):                                  #           *
    for j in range(5-i-1):                          #         * *
        print(" ",end=" ")                          #       * * *
    for k in range(i+1):                            #     * * * *
        print("*",end=" ")                          #   * * * * *
    print()

print("6".center(15," "))

for i in range(5):                                  #   * * * * *  
    for j in range(i):                              #     * * * *  
        print(" ",end=" ")                          #       * * *
    for k in range(5-i):                            #         * *
        print("*",end=" ")                          #           *
    print()

print("6.1".center(15," "))

for i in range(5):
    print(" "*i + " ",end=" ")
    print("*"*(5-i) + " ",end=" ")
    print()




print("7".center(15," "))

for i in range(5):                                  #   *    
    for j in range(i+1):                            #   * *    
        print("*",end=" ")                          #   * * *    
    print()                                         #   * * * *    
                                                    #   * * * * *

print("8".center(15," "))

#n=int(input("Enter number : "))                    
for i in range(9):                                  #   *      
    if i<9/2:                                       #   * *     
        for j in range(i+1):                        #   * * *     
            print("*",end=" ")                      #   * * * *     
        print()                                     #   * * * * *     
    else:                                           #   * * * *     
        for k in range(9-i):                        #   * * *     
            print("*",end=" ")                      #   * *     
        print()                                     #   *

'''
print("9".center(15," "))

n=int(input("Enter num : "))
m=n//2
for i in range(n):                                  #       *          
    if i<n/2 and n%2==0:                            #     * *           
        for j in range(m-i-1):                      #   * * *           
            print(" ",end=" ")                      #   * * *           
        for k in range(i+1):                        #     * *           
            print("*",end=" ")                      #       *
        print()

    elif i<n/2 and n%2!=0:                          #       * 
        for j in range(m+1-i-1):                    #     * *    
            print(" ",end=" ")                      #   * * *
        for k in range(i+1):                        #     * *
            print("*",end=" ")                      #       *
        print()
                                            
    else:                                    
        for j in range(i-m):                
            print(" ",end=" ")                            
        for k in range(n-i):                              
            print("*",end=" ")
        print()


        * 
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *


'''
'''
print("10".center(15," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("10.1".center(15," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("10.2".center(15," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("11--Z".center(15," "))
#logic is sum(i+j)
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("12--X".center(15," "))
#logic is sum(i+j)
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("13--I".center(15," "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print("14--H".center(15," "))

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

print()
print("Groceries : ".center(20," "))


data = {
    1:{'name':'Rice','price':60},
    2:{'name':'Wheat Flour','price':45},
    3:{'name':'sugar','price':35},
    4:{'name':'Milk','price':30},
    5:{'name':'Eggs (12 pcs)','price':60},
    6:{'name':'Oil','price':130},
    7:{'name':'Tea Powder','price':25},
    8:{'name':'Salt','price':15},
    9:{'name':'Bread','price':35},
    10:{'name':'Soap','price':45}
}

for i in data:
    print(f'{i}. {data[i]['name']} - Rs.{data[i]['price']}')

items=list(map(int,input("Select your Products (1 2 3) : ").split()))

total=0
s=set()

for i in items:
    if i not in s:
        c=items.count(i)
        print(f'{data[i]['name'].center(15," ")} - {data[i]['price']} * {c} = {data[i]['price' ] * c}')
        total+=data[i]['price']*c
        s.add(i)
print(f'Total Bill: Rs.{total}')


#total=0
#d={
#    'milk':60,
#    'rice':70,
#    'oil':130,
#    'wheat':40
#}
#
#while True:
#    product_name=input("Enter Products : ").lower()
#    if product_name=='0':
#        break
#    quantity=int(input("Enter Quantity :"))
#    total+=d[product_name] * quantity
#
#
#print(f'Rs. {total}')

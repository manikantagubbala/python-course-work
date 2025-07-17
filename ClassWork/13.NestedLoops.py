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

'''
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



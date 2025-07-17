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





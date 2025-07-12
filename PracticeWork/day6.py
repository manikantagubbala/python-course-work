#print("Palindrome".center(15," "))
#a=input("Enter list values : ").lower().split()
#n=0
#for i in a:
#    if a[n] == a[n][::-1]:
#        print(f'{a[n]} is a Palindrome')
#        break
#    n+=1
#else:
#    print(f'In this list have no Palindromes.')


#n=int(input("Enter the number : "))
#for i in range(1,n+1):
#    if i%2==0:
#        print(f'{i} is an Even number.')
#        break
#else:
#    print(f'{i} is an odd number.')
       

n=int(input("Enter the number : "))
c=0
for i in range(1,n+1):
    if i%7==0:
        print("Stop")
        break
    c+=1
    print(c)
   

#a=list(map(str,input().split()))
#for i in a:
#    print(i)    


n=int(input("Enter number : "))
for i in range(n,0,-1):
    print(i)
    if i==2:
        print("Stoped at 2")
        break
else:
    print("Done")
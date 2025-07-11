#print("Even or Odd".center(20," "))
#a = int(input())
#if a%2==0:
#    print("Even")
#else:
#    print("Odd")


#a = int(input("Enter number : "))
#if a>0:
#    print("Positive")
#elif a<0:
#    print("Negative")
#else:
#    print("Zero")

print("Leaf Year".center(30)," ")
year=int(input("Enter number : "))
if year%400==0 or year%4==0 and year%100!=0:
    print(f'{year} is Leaf year')
else:
    print(f'{year} is not a Leaf year')
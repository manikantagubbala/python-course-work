# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
n=int(input())
num1=set(map(int,input().split()))
m=int(input())
num2=set(map(int,input().split()))


c=num1.union(num2)
print(len(c))
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
n=int(input())

for i in range(n):
    b=set(map(int,input().split()))
    
print(a.issuperset(b))
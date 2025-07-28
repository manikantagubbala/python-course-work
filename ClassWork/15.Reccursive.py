print()
def display(s,ind):
    if ind==len(s):
        return 
    print(s[ind])
    return display(s,ind+1)
s="Python Programming"
display(s,0)

def display(s,ind):
    if ind==-1:
        return
    print(s[ind],end="")
    display(s,ind-1)
s="python"
display(s,len(s)-1)
print()

def sod(n):
    if n<=0:
        return n
    return (n%10) + sod(n//10)
print(sod(int(input("Enter number: "))))
# Module
import Assignment4 as asg

while True:
    op = int(input("Enter a number: "))
    if op == 0:
        break
    elif op==1:
        asg.check_leafYear()

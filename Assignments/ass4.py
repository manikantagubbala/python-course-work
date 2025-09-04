# Module
import Assignment4 as asg

while True:
    op = int(input("Enter an Option: "))
    if op == 0:
        break
    elif op==1:
        num = int(input("Enter a number: "))
        asg.check_leafYear(num)
    elif op==2:
        print(asg.longest_word())
    elif op==3:
        asg.count_freq()
    elif op==4:
        asg.sum_of_nums()
    elif op==5:
        asg.str_comp()
    #elif op==6:
    #elif op==7:
    #elif op==8:
    #elif op==9:
    #elif op==10:
#

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
        word = input("Enter a Sentence: ").split()
        print(asg.longest_word(word))
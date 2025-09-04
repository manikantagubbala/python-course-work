# Module
import Assignment4 as asg

def questions():
    print("\n1.Check Leap Year \nInput: 2024 → Output: Leap Year.\n")
    print("2.Find Longest Word in a Sentence \nInput: 'Accenture hiring challenges' → Output: 'challenges'.\n")
    print("3.Count Frequency of Each Character in String \nInput: 'success' → Output: s:3, u:1, c:2, e:1.\n")
    print("4.Find Sum of N Natural Numbers Without Loop \nInput: 10 → Output: 55 \nFormula used: n*(n+1)/2.\n")
    print("5.String Compression \nInput: 'aaabbcddd' → Output: 'a3b2c1d3'\n")
    print("6.Check Harshad (Niven) Number \nA number divisible by the sum of its digits. \nExample: 18 → 1+8=9 → 18%9=0 → Harshad\n")
    print("7.Check Strong Number \nA number is strong if the sum of factorials of its digits equals the number. \nExample: 145 → 1! + 4! + 5! = 145\n")
    print("8.Floyd’s Triangle \n1  \n2 3 \n4 5 6 \n7 8 9 10\n")
    print("9.Reverse a String without using built-in functions \nInput: 'hello' → Output: 'olleh'\n")
    print("10.Count Vowels and Consonants in a String \nInput: 'python' → Vowels: 1, Consonants: 5 ")

while True:
    questions()
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
    elif op==6:
        asg.check_niven()
    elif op==7:
        asg.check_strong()
    elif op==8:
        asg.floyd_pattern()
    elif op==9:
        asg.reverse_str()
    elif op==10:
        print(asg.count_vow_con())
    else:
        print("You can choose correct Option")
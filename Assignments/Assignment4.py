# 10 Coding questions

# 1.Check Leap Year
# Input: 2024 → Output: Leap Year.

def check_leafYear(num):
    if num%400 == 0 and num%4 == 0 or num%100 != 0:
        print(f'Leaf Year')
    else:
        print("It is not a Leaf Year")



# 2.Find Longest Word in a Sentence
#Input: "Accenture hiring challenges" → Output: "challenges".

def longest_word():
    word = input("Enter a Sentence: ").split()
    long_word = {}
    for i in word:
        long_word[i] = len(i)
    longest_word_sen = max(long_word, key=long_word.get)
    return longest_word_sen



# 3.Count Frequency of Each Character in String
#Input: "success" → Output: s:3, u:1, c:2, e:1.

def count_freq():
    word = input("Enter a word: ")
    count_word = {}
    for i in word:
        count_word[i] = word.count(i)
    print(count_word)


# 4.Find Sum of N Natural Numbers Without Loop
# Input: 10 → Output: 55
# Formula used: n*(n+1)/2.


def sum_of_nums():
    n = int(input("Enter a number: "))
    print(int(n*(n+1)/2))


# 5.String Compression
# Input: "aaabbcddd" → Output: "a3b2c1d3"


def str_comp():
    word = input("Enter a String: ")
    result = ""
    for i in word:
        if i not in result:
            result += i + str(word.count(i))
    print(result) 


# 6.Check Harshad (Niven) Number
# A number divisible by the sum of its digits.
# Example: 18 → 1+8=9 → 18%9=0 → Harshad


def check_harsad(num):
    sum = 0
    while num>0:
        digit = num % 10
        sum += digit
        num = num//10    
    return sum
num = int(input("Enter the number: "))
def check_niven():
    if num % check_harsad(num) == 0:
        print("Harshad")
    else:
        print("Not Harshad")

'''
# 7.Check Strong Number
# A number is strong if the sum of factorials of its digits equals the number.
# Example: 145 → 1! + 4! + 5! = 145


import math
def check_strong_num(num):
    sum_of_fact = 0
    while num>0:
        digit = num%10
        sum_of_fact += math.factorial(digit)
        num = num//10
    return sum_of_fact
num = int(input("Enter Number: "))
def check_strong():
    if num == check_strong_num(num):
        print(f"{num} is Strong Number.")
    else:
        print(f"{num} is not a Strong Number.")


# 8.Floyd’s Triangle
# 1 
# 2 3
# 4 5 6
# 7 8 9 10

def floyd_pattern(rows):
    start = 1
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(start, end=" ")
            start += 1
        print()
rows = int(input("Enter Range You want:\n"))


# 9.Reverse a String without using built-in functions
# Input: "hello" → Output: "olleh"


def reverse_str(s):
    rev = ""
    for i in s:
        rev = i + rev
    print(rev)
s = input("Enter the string: ")


# 10.Count Vowels and Consonants in a String
# Input: "python" → Vowels: 1, Consonants: 5

def count_vow_con(word):
    vowels = 'aeioiu'
    v = 0
    c = 0
    for i in word:
        if i in vowels:
            v += 1
        else:
            c += 1
    print(f'Vowels: {v}\nConsonants: {c}')
word = input("Enter the Word: ").lower()
print(count_vow_con(word))

'''
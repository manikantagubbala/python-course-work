# 10 Coding questions

# 1.Check Leap Year
# Input: 2024 → Output: Leap Year.
'''
def check_leafYear(num):
    if num%400 == 0 and num%4 == 0 or num%100 != 0:
        return f'Leaf Year'
    else:
        return "It is not a Leaf Year"

num = int(input("Enter a number: "))
print(check_leafYear(num))

'''
# 2.Find Longest Word in a Sentence

#Input: "Accenture hiring challenges" → Output: "challenges".
'''
def longest_word(word):
    long_word = {}
    for i in word:
        long_word[i] = len(i)
    return max(long_word, key=long_word.get)

word = input("Enter a Sentence: ").split()
print(f'Output: {longest_word(word)}')

'''

# 3.Count Frequency of Each Character in String
#Input: "success" → Output: s:3, u:1, c:2, e:1.
'''
def count_freq(word):
    count_word = {}
    for i in word:
        count_word[i] = word.count(i)
    return count_word
word = input("Enter a word: ")
print(count_freq(word))
'''

# 4.Find Sum of N Natural Numbers Without Loop
#Input: 10 → Output: 55
#Formula used: n*(n+1)/2.
'''
def sum_of_nums(n):
    return int(n*(n+1)/2)
n = int(input("Enter a number: "))
print(sum_of_nums(n))
'''


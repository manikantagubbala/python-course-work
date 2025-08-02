print(" QUIZ GAME ".center(30,"*"))

quiz={
    1:{
        "Question": "Question 1: What is the output of: print(type([]))?",
        'a':"a) <class 'list'>",
        "b":"b) <class 'dict'>",
        'c':"c) <class 'set'>",
        "d":"d) <class 'tuple'>"
    },
    2:{
        "Question": "Queation 2: Which keyword is used to define a function in Python?",
        'a':"a) function",
        "b":"b) def",
        'c':"c) fun",
        "d":"d) define"
    }
}

num=int(input())
count=0
for i in range(1,num+1):
    print(quiz[i]['Question'])
    print(quiz[i]['a'])
    print(quiz[i]['b'])
    print(quiz[i]['c'])
    print(quiz[i]['d'])
    if i==1:
        option=input("Enter your answer: ")
        if option=='a':
            count+=1
            print("✅ Correct! \n")
        else:
            print("❌ Wrong! The correct answer is 'a' \n")
    
    if i==2:
        option=input("Enter your answer: ")
        if option=='b':
            count+=1
            print("✅ Correct! \n")
        else:
            print("❌ Wrong! The correct answer is 'b' \n")


print(f"🎯 Your Final Score: {count}/10")
print("🎉 Great job! Keep practicing!")
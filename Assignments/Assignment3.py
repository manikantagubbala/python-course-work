print(" QUIZ GAME ".center(30,"*"))

quiz={
    1:{
        "Question": "Question 1: What is the output of: print(type([]))?",
        'a':"a) <class 'list'>",
        "b":"b) <class 'dict'>",
        'c':"c) <class 'set'>",
        "d":"d) <class 'tuple'>",
        "answer":'a'
    },
    2:{
        "Question": "Queation 2: Which keyword is used to define a function in Python?",
        'a':"a) function",
        "b":"b) def",
        'c':"c) fun",
        "d":"d) define",
        "answer":'b'
    },
    3:{
        "Question": "Question 3: What is the output of 3 * '5'?",
        "a":"a) 15",
        "b":"b) 555",
        "c":"c) Error",
        "d":"d) None",
        "answer":'b'
    },
    4:{
        "Question": "Question 4: Which of the following is **immutable**?",
        "a":"a) list",
        "b":"b) dict",
        "c":"c) set",
        "d":"d) tuple",
        "answer":'d'
    },
    5:
    {
        "Question": "Question 5: How do you start a comment in Python?",
        "a":"a) //",
        "b":"b) <!",
        "c":"c) #",
        "d":"d) **",
        "answer":'c'
    },
    6:{
        "Question": "Question 6: What does len() do in Python?",
        "a":"a) Calculates size of int",
        "b":"b) Returns list length",
        "c":"c) Finds memory usage",
        "d":"d) Loops through list",
        "answer":'b'
    },
    7:{
        "Question": "Question 7: What is the correct file extension for Python files?",
        "a":"a) .pt",
        "b":"b) .python",
        "c":"c) .py",
        "d":"d) .pyt",
        "answer":'c'
    },
    8:{
        "Question": "Question 8: Which of the following is used to import a module?",
        "a":"a) include",
        "b":"b) import",
        "c":"c) using",
        "d":"d) require",
        "answer":'b'
    },
    9:{
        "Question": "Question 9: What is the output of bool(0)?",
        "a":"a) True",
        "b":"b) False",
        "c":"c) 0",
        "d":"d) None",
        "answer":'b'
    },
    10:{
        "Question": "Question 10: What is used to define a block of code in Python?",
        "a":"a) Brackets {}",
        "b":"b) Parentheses ()",
        "c":"c) Indentation",
        "d":"d) Curly braces",
        "answer":'c'    
    }
}


#num=int(input())
count=0
options=1
for i in range(1,len(quiz)+1):
    print(quiz[i]['Question'])
    print(quiz[i]['a'])
    print(quiz[i]['b'])
    print(quiz[i]['c'])
    print(quiz[i]['d'])
    if i==options:
        option=input("Enter your answer: ").strip().lower()
        if option==quiz[i]["answer"]:
            count+=1
            print("✅ Correct! \n")
        else:
            print(f"❌ Wrong! The correct answer is {quiz[i]['answer']} \n")
    options+=1



print(f"🎯 Your Final Score: {count}/{len(quiz)}")
print("🎉 Great job! Keep practicing!")
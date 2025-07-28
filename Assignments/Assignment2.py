print("Chat Data Analysis".center(40," "))
chat={}
n=int(input("Enter the no.of messages: "))

for i in range(n):
    name,msg=input().split(":")
    if name in chat:
        chat[name].append((msg,i))
    else:
        chat[name]=[(msg,i)]

print(chat)
print(chat.values())
print(len(chat.values()))


def total_msgs():
    print(f'Total Messages: {n}')

def unique_users(chat):
    print(f'unique users in the chat: {set(chat.keys())}')

def total_word(chat):
    global length
    length=0
    for messages in chat.values():
        for msg, _ in messages:
            length += len(msg.split())
    return length

def average_words():
    average=total_word(chat)/n
    print(f'Average words per message: {average:.2f}')

def long_msg(chat):
    for i in chat.values():
        for msg,_ in i:
            long=0
            if long>len(msg.split()):
                msg
    print(f'Longest message in the chat: {msg}')

def most_user(chat):
    l=0
    user=""
    for i in chat:
        if l<len(chat[i]):
            l=len(chat[i])
            user=i
    print(f'Most Active User in the chat: {user} ({l}messages)')

def count_spf_user(chat):
    name=input("Enter a specific user: ").capitalize()
    if name in chat:
        print(f'Message Count for Specific user: {len(chat[name])}')

while True:
    print("0.Exit")
    print("1. Count total number of messages: ")
    print("2. Identify unique users in the chat: ")
    print("3. Count total words in the chat: ")
    print("4. Calculate average words per message: ")
    print("5. Find the longest message sent: ")
    print("6. Find the most active user: ")
    print("7. Get message count for a specific user: ")
    print("8. Find the most frequently used word by a specific user: ")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat: ")
    print("11. Find commonly repeated words: ")
    print("12. Identify the user with the longest average message length: ")
    print("13. Count how many messages mention a specific user: ")
    print("14. Remove duplicate messages: ")
    print("15. Sort messages alphabetically: ")
    print("16. Extract all questions asked in the chat: ")
    print("17. Calculate the reply ratio between two users: ")
    print("18. Check for deleted messages")

    op=int(input("You can choose option: "))
    if op==0:
        print("Invalid Choice.")
        break
    elif op==1:
        total_msgs()
    elif op==2:
        unique_users(chat)
    elif op==3:
        print(f'Total words in this chat: {total_word(chat)}')
    elif op==4:
        average_words()
    elif op==5:
        long_msg(chat)
    elif op==6:
        most_user(chat)
    elif op==7:
        count_spf_user(chat)
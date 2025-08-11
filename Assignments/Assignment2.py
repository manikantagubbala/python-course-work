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
print(chat.keys())
print("Values: ", chat.values())
print(len(chat.values()))


def total_msgs():
    print(f'Total Messages: {n}')

def unique_users(chat):
    print(f'unique users in the chat: {set(chat.keys())}')

def total_word(chat):
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
            if long>len(msg):
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
  
                
def first_and_last_msg(chat):
    name = input("Enter the Name in the Chat: ").capitalize()
    first_msg=[]
    if name in chat:
        for msg,i in chat[name]:
            first_msg.append(msg)
    print(f'First message by {name}: "{name}: {first_msg[0]}" ')
    print(f'Last message by {name}: "{name}: {first_msg[len(first_msg) - 1]}" ')


def user_is_present(chat):
    name = input("Enter a specific Username: ").capitalize()
    if name in chat.keys():
        print(f"User '{name}' found in the chat.")
    else:
        print(f"User '{name}' not found in the chat.")


def common_repeated_words(chat):
    words=[]
    for i in chat.values():
        for msg,j in i:
            word = msg.split()
            words.append(word)

    common = []
    for i in words:
        for j in i:
            common.append(j)

    repeated_words = {}
    for i in common:
        if i not in repeated_words:
            repeated_words[i] = common.count(i)
    print(max(repeated_words,key=repeated_words.get))


def longest_avg_msg(chat):
    for i in chat.values():
        for msg,j in i:
            long=0
            if long>len(msg):
                msg
    longest_msg = [msg.split()]
    print(len(longest_msg))

def count_messages_spec_user(chat):
    name = input("Enter the specific Username: ").capitalize()
    print(f"Messages mentioning '{name}': {len(chat[name])} ")


def sort_messages(chat):
    sort_msg = []
    for i in chat.values():
        for msg,j in i:
            sort_msg.append(msg)
    print(sorted(sort_msg))


def question_msg(chat):
    question = []
    for i in chat.values():
        for msg,j in i:
            if msg[-1] == "?":
                question.append(msg)
    print(question)


def deleted_messages(chat):
    del_msg_count = 0
    for i in chat.values():
        for msg,j in i:
            if msg=="This message was deleted":
                del_msg_count += 1
    print(f"Deleted messages found: {del_msg_count}")


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
    elif op==9:
        first_and_last_msg(chat)
    elif op==10:
        user_is_present(chat)
    elif op==11:
        common_repeated_words(chat)
    elif op==12:
        longest_avg_msg(chat)
    elif op==13:
        count_messages_spec_user(chat)
    elif op==15:
        sort_messages(chat)
    elif op==16:
        question_msg(chat)
    elif op==18:
        deleted_messages(chat)

print("Remaining questions: 8,14,17")
#14.function.py

'''
syntax : 
        def fun():
            //statements
            return 
        print()

'''
print("Function".center(15," "))

data = {'current_balance':1000, 'history':[]}
def check_balance():
    print(f'Current Balance: {data['current_balance']}')

def deposit():
    amount=int(input("Enter you want to Depoit: "))
    data["current_balance"]+=amount
    data["history"].append(f'Deposit - Rs.{amount}')
    print(f'Amount deposited Successfully - Rs.{amount}')
    print(f'Current Balance: {data["current_balance"]}')

def withdraw():
    amount=int(input("Enter Withdraw amount: "))
    if amount<data["current_balance"]:
        data['current_balance']-=amount
        data["history"].append(f'Withdraw - Rs.{amount}')
        print(f'Withdraw Successfully - Rs.{amount}')
    else:
        print("Insuffiecent Balance")
    print(f'Current Balance: {data["current_balance"]}')

def history():
    print("Transactions: ".center(20,"*"))
    for i in data['history']:
        print(i)

#Menu-Driven

while True:
    print()
    print("1.CheckBalance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.history")
    print("5.Exit")

    op=int(input("Enter u want: "))
    if op==0:
        print("Thank You ")
        break
    elif op==1:
        check_balance()
    elif op==2:
        deposit()
    elif op==3:
        withdraw()
    elif op==4:
        history()
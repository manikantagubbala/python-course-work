#Logic Program

data={
    12345:{"pin":1234, "balance":1000, "history":[]},
    23456:{"pin":2345, "balance":1000, "history":[]},
    34567:{"pin":3456, "balance":1000, "history":[]},
    45678:{"pin":4567, "balance":1000, "history":[]},
    56789:{"pin":5678, "balance":1000, "history":[]}
}

def Welcome():
    print("Welcome to ATM".center(50,"*"))
    print()

def Login():
    global account_num
    account_num=int(input("Enter Account Number: "))
    global pin
    pin=int(input("Enter your pin: "))
    if account_num in data:
        if data[account_num]["pin"]==pin:
            print("Login Successful")
            return True
        else:
            print("Invalid PIN")
            return False
    else:
        print("Invalid Account Number")
        return False

def Menu():
    print()
    print("[c]heckBalnace")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[M]ini Statement")
    print("[E]xit")

def check_balance():
    if account_num in data:
        print(f"Current Balance: {data[account_num]["balance"]}")

def deposit():
    if account_num in data:
        amount=int(input("Enter Deposit amount: "))
        data[account_num]["balance"]+=amount
        data[account_num]["history"].append(f"Deposit sucessfull Rs.{amount}")

def withdraw():
    if account_num in data:
        amount=int(input("Enter Withdraw amount: "))
        if amount<=data[account_num]["balance"]:
            data[account_num]["balance"]-=amount
            data[account_num]["history"].append(f"Withdraw successfull Rs.{amount}")

def Mini_Statement():
    if account_num in data:
        print("Transactions".center(40,"-"))
        for i in data[account_num]["history"]:
            print(i)
        print("End of the Transactions".center(40,"-"))
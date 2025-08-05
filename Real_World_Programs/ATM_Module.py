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
    account_num=int(input("Enter Account Number: "))
    pin=int(input("Enter your pin: "))
    if account_num in data:
        if data[account_num]["pin"]==pin:
            print("Login Successful")
        else:
            print("Invalid PIN")
    else:
        print("Invalid Account Number")
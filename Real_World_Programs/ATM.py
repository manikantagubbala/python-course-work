#Main Program
import ATM_Module as atm

atm.Welcome()

if atm.Login():
    while True:
        atm.Menu()
        option=input("Enter your choice in Menu: ").upper()
        if option=='C':
            atm.check_balance()
        elif option=='D':
            atm.deposit()
        elif option=='W':
            atm.withdraw()
        elif option=="M":
            atm.Mini_Statement()
        elif option=="E":
            print("Thankyou".center(50,"_"))
            break
seats={
    'L1':True,
    'L2':True,
    'u1':False,
    'U2':True
}

print(seats.keys())

sid=input("Enter seat Id : ").upper()
if sid in seats:
    if seats[sid]:
        print("Seat is available. You can Book now")
    else:
        print("Seats are not available")
else:
    print("You can choose correct one.")
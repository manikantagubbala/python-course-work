print("Zomato".center(25,"-"))

booking_id = input("Enter the Booking Id : ")
item_name = input("Show Item Name : ")
item_price = float(input("Show Item Price : "))
discount_price = float(input("Discount Price : "))
delivery_distance = float(input("Show the distance : "))
delivery_charges = int(input("Enter the Delivery Charges : "))
delivery_boy_name = input("Enter Delivery Boy Name : ")
delivery_contact = int(input("Contact Number : "))
delivery_location = input("Enter your Location : ")

total_price = item_price - discount_price + delivery_charges 

print("\nBooking ID : ",booking_id, "\nItem : ", item_name,"\nPrice : ", item_price)

print("Discount %2f" %(discount_price) + "%")

print(f'Distance : {delivery_distance} km \nDelivery Charges : {delivery_charges} \nPerson Name :{delivery_boy_name}')

print("Contact Number : +91 {} \nLocation : {}".format(delivery_contact, delivery_location))

print(f'Total Price : Rs.{total_price}')
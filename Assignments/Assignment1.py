print("Zepto Store".center(25,"-"))

bill_id = input("Enter the Booking Id : ")
item_name = input("Enter Item Name : ")
item_price = float(input("Enter Item Price : "))
categories = input("Enter Categories : ").split(",")
discount_price = float(input("Discount Price : "))
delivery_distance = float(input("Enter the distance : "))
delivery_charges = int(input("Enter the Delivery Charges : "))
delivery_boy_name = input("Enter Delivery Boy Name : ")
delivery_contact = int(input("Contact Number : "))
delivery_location = input("Enter your Location : ")

total_price = item_price - discount_price + delivery_charges 

print(f'Available Categories in Store : {categories}')

print("\Bill ID : ",bill_id, "\nItem : ", item_name,"\nPrice : ", item_price)

print("Discount %2f" %(discount_price) + "%")

print(f'Distance : {delivery_distance} km \nDelivery Charges : {delivery_charges} \nPerson Name :{delivery_boy_name}')

print("Contact Number : +91 {} \nLocation : {}".format(delivery_contact, delivery_location))

print(f'Total Price : Rs.{total_price}')





'''

class -- ZeptoStore,  
child_class -- Dmart, Reliance
methods -- Groceries, Vegetables, Fruits
attribute -- itemname, brand
super() -- same items in both stores



'''






#integer
a = 10
print(type(a))      

#float
a = 10.0
print(type(a))     

#complex
a = 3+3j
print(type(a))       

#string
name = 'aditya'
print(type(name))

#list
cart_items = ["shoes","T-shirts","headphones","shoes"]
print(type(cart_items))                      # list and it will add and del values
print(cart_items)                            # it can maintain duplicate values
cart_items.append(["paper",10])              # it can maintain same order 
print(cart_items)                            # list is mutable
print(type(cart_items))

#tuple
warehouse_location = (12.9716, 77.5946)
print(type(warehouse_location))           #tuple and can't add and del values and it can also immutable
print(warehouse_location)                 # it can maintain duplicate values and same order 

#set
available_sizes = {"s","d","c"}
print(type(available_sizes))                #set is a order & unorder and mutable and it doesn't allow duplicate values
available_sizes.add('g')
print(available_sizes)

#frozenset
frozen_tags = frozenset(["sale","trending"])
print(type(frozen_tags))                    #frozenset
print(frozen_tags)

#dictionary
product_details ={
    "name": "wireless mouse",
    "brand": "asus",
    "price": 699
}
print(type(product_details))               #dictionary it can add & del values and mutable and it doesn't allow duplicate values

#boolean
logged_in = True
payment_successful = False
in_stock = True
print(type(in_stock))                    

#nontype
tracking_number = None
delivery_partner = None
print(type(tracking_number))
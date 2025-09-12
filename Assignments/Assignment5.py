# Developing Zepto Store

'''

---> Fruits 
        -> Apple, Banana, Grapes, CustardApple, Papaya
---> Vegetables
        -> Potato, Brinjal, Beetroot, Carrot, SweetPotato
---> Groceries
        -> Rice, Oil, Atta, Ghee, Dals

'''

import random

#class Deliver:
#    def __init__(self, names):
#        self.name = names
#        print(random.choice(self.name))
#
#names = ["Praneeth", "Kamal", "Vimal", "Nihal", "Mohit"]
#deliver_name = Deliver(names)



class Product:
    """Base class for all products in the Zepto store"""
    def __init__(self, name, price, quantity=1):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setter
    def set_quantity(self, qty):
        if qty >= 0:
            self.__quantity = qty
        else:
            print("Quantity cannot be negative!")

    def __str__(self):
        return f"{self.__name} - ₹{self.__price} per kg (Available: {self.__quantity} kg)"


class Fruits(Product):
    pass


class Vegetables(Product):
    pass


class ZeptoStore:
    def __init__(self):
        self.fruits = [
            Fruits("Apple", 120, 10),
            Fruits("Banana", 60, 20),
            Fruits("Mango", 150, 5)
        ]
        self.vegetables = [
            Vegetables("Potato", 30, 25),
            Vegetables("Carrot", 40, 15),
            Vegetables("Brinjal", 35, 10)
        ]
        self.cart = []

    def show_products(self):
        print("\n--- Fruits ---")
        for i, fruit in enumerate(self.fruits, start=1):
            print(f"{i}. {fruit}")

        print("\n--- Vegetables ---")
        for j, veg in enumerate(self.vegetables, start=1):
            print(f"{j}. {veg}")

    def add_to_cart(self, category, index, qty):
        if category == "fruit":
            product_list = self.fruits
        elif category == "veg":
            product_list = self.vegetables
        else:
            print("❌ Invalid category!")
            return

        if 0 < index <= len(product_list):
            product = product_list[index - 1]
            if product.get_quantity() >= qty:
                product.set_quantity(product.get_quantity() - qty)
                self.cart.append((product.get_name(), qty, product.get_price() * qty))
                print(f"✅ Added {qty} kg {product.get_name()} to cart")
            else:
                print("❌ Not enough stock!")
        else:
            print("❌ Invalid product number!")

    def show_cart(self):
        print("\n🛒 Your Cart:")
        if not self.cart:
            print("Cart is empty.")
            return
        total = 0
        for item in self.cart:
            print(f"- {item[0]} : {item[1]} kg = ₹{item[2]}")
            total += item[2]
        print(f"Total Bill: ₹{total}")
        

def main():
    store = ZeptoStore()
    print("=== Welcome to Zepto Store ===")

    while True:
        print("\nChoose an option:")
        print("1. Show Available Products")
        print("2. Add Fruit to Cart")
        print("3. Add Vegetable to Cart")
        print("4. View Cart")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            store.show_products()
        elif choice == "2":
            store.show_products()
            try:
                index = int(input("Enter fruit number: "))
                qty = int(input("Enter quantity (kg): "))
                store.add_to_cart("fruit", index, qty)
            except ValueError:
                print("❌ Please enter valid numbers.")
        elif choice == "3":
            store.show_products()
            try:
                index = int(input("Enter vegetable number: "))
                qty = int(input("Enter quantity (kg): "))
                store.add_to_cart("veg", index, qty)
            except ValueError:
                print("❌ Please enter valid numbers.")
        elif choice == "4":
            store.show_cart()
        elif choice == "5":
            print("🙏 Thank you for shopping at Zepto Store!")
            break
        else:
            print("❌ Invalid choice, try again.")


# Run program
if __name__ == "__main__":
    main()

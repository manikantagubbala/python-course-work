from abc import ABC,abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class FoodOrder(Order):
    def process_order(self):
        print("You are hungry, You can order Biryani.")

class GroceryOrder(Order):
    def process_order(self):
        print("You need Groceries, then you can buy Groceris.")

order = FoodOrder()
order.process_order()

order = GroceryOrder()
order.process_order()
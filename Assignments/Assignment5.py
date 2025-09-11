# Developing Zepto Store

'''

---> Fruits 
        -> Apple, Banana, Grapes, CustardApple, Papaya
---> Vegetables
        -> Potato, Brinjal, Beetroot, Carrot, SweetPotato
---> Groceries
        -> Rice, Oil, Atta, Ghee, Dals

'''


class Fruits:
    def fruit_1(self):
        self.fruit1 = "Apple"
        print(self.fruit1)

class Vegetables:
    def veg(self):
        vegetable_list = {
            1 : {"name" : "Potato", "price" : 30, "quantity" : 1},
            2 : {"name" : "Brinjal", "price" : 35, "quantity" : 1},
            3 : {"name" : "Beetroot", "price" : 15, "quantity" : 1},
            4 : {"name" : "Carrot", "price" : 20, "quantity" : 1},
            5 : {"name" : "SweetPotato", "price" : 25, "quantity" : 1},
        }
        print(f"")

class Products(Fruits,Vegetables):
    print("Show Available Products in the Zepto Store")

product = Products()
product.fruit_1()
print(product.veg())
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ShoppingCart:
    def __init__(self,name,address,number):
        self.name=name
        self.address=address
        self.number=number
        self.cart = []
        print(f"Hello {self.name},you have successfully opened new account ")

    def display_cart(self):
        if not self.cart:
            print("your cart is empty")
        else:
            print("Shopping cart")
        total_price=0
        for item in self.cart:
            print(f"{item['name']}: ${item['price']}")
            total_price+=item['price']
        print(f"total : ${total_price}")

    def Add_item(self):
        item_name = input("Enter the item name :")
        item_price = float(input("Enter item Price :"))
        item = {"name": item_name, "price": item_price}
        self.cart.append(item)
        print("item added to cart")

    def Remove_item(self):
        if not self.cart:
            print("Your cart is empty")
        else:
            ShoppingCart.display_cart(self)
            item_index = int(input("Enter the item number to remove"))
            if 0 <= item_index < len(self.cart):
                removed_item = self.cart.pop(item_index)
                print(f"Removed item : {removed_item['name']}")
            else:
                print("invalid index num")
    def main(self):
        while True:
            print("\n Shopping Cart Application")
            print("1.Add item to Cart\n2.View cart \n3.Remove Item from Cart \n4.Exit")
            choice=int(input("Enter your Choice"))
            if choice==1:
                ShoppingCart.Add_item(self)
            elif choice==2:
                ShoppingCart.display_cart(self)
            elif choice==3:
                ShoppingCart.Remove_item(self)
            elif choice==4:
                break
            else:
                print("Plese enter valid option")


name=input("enter the name")
address=input("enter the address")
number=int(input("Enter the number"))
Preethi=ShoppingCart(name,address,number)
Preethi.main()


# In[ ]:





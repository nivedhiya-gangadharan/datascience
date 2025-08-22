# items=["apple","mango","grapes"]
# print(items[0])
# print(items[1:3])
# items.append("milk")
# print(items)
# demo=input("enter the product to be searched:")
# if demo in items:
#     print("its there in items")
# else:
#     print("its not there in items")
# items.remove("milk")
# print(items)
# while True:
#     print("1. Add 2.remove 3.View 3. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         it = input("Enter the item: ")
#         items.append(it)

#     elif choice == "2":
#         rt=input("enter the item to be removed:")
#         items.remove(rt)

        
#     elif choice == "3":
#         print("Current items:", items)

    
#     elif choice == "4":
#         print("Exiting the program.")
#         break

#     else:
#         print("Invalid choice")

product=[]
items=int(input("no of products"))
for i in range (items):

    name=input("enter the product ")
    quantity=int(input("enter the quantity"))
    price=int(input("enter the price:"))

    if price >50:
        discount=price*.5
        price-=discount


    product.append({
        "name":name,
        "quantity":quantity,
        "price":price,
    })
print(product)

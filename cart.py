cart=[]
print("--shopping cart---")
print("1.add product")
print("2.remove product")
print("3.update product") 
print("4.view product")
print("5.search") 
print("6.slice") 
print("7.sort")
print("8.exit") 
cart.append("book")
cart.append("pencil")
cart.append("eraser")
cart.append("pen")
cart.remove("pen")
cart[0]="pen"
print("your cart items")
for item in cart:
    print("-",item)
print(cart[0:2])
print(len(cart))

print(cart)
product=input("enter the element to be searched")
if product in cart:
    print("it is in the cart")
else:
    print("its not in the cart")



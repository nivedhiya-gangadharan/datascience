a=["milk","bread","egg"]
b=[40,25,5]
total_amount=0
demo=int(input("enter the number of products:"))
for i in range (demo):
    item=input("enter the item name:")
    quantity=int(input("enter the quantity:"))
    if item in a:
        index=a.index(item)
        amount=b[a.index(item)]*quantity
    total_amount=total_amount+amount
    if total_amount>500:
        discount=total_amount*0.1
        total_amount-=discount
    elif total_amount>1000:
        discount=total_amount*0.2
        total_amount-=discount
print("total amount=",total_amount)

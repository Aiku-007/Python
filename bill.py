def grocery_bill(price,quantity):
    total=price*quantity
    if total>100:
        discount=total*10/100
        final_price=total-discount
        return final_price
    else:
        return total


print(grocery_bill(20, 3))
print(grocery_bill(25, 5))

price=int(input("Enter the price: "))
quantity=int(input("Enter the quantity: "))
print(grocery_bill(price,quantity))


      
    

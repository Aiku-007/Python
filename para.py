def login(username="Guest"):
    print("welcome",username)

login("Aiko")
login()

def discount(price,discount_percent=10):
    final_price=price*discount_percent/100
    return final_price

print(discount(200))
print(discount(100,25))
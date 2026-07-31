def withdraw(balance,amount):
    if amount>balance:
        return "Insufficient Balance"
    else:
        remaining_balance=balance-amount
        return remaining_balance
print(withdraw(1000, 300))
print(withdraw(500, 700))

balance=float(input("My balance: "))
amount=float(input("Withdrawal amount: "))
print(withdraw(balance,amount))

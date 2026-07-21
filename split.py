print("--Bill Spliter--")

#1. Get inputs from the user
bill_amount = float(input("Enter the total bill amount: "));

#we use int for whole numbers
tip_percentage = int(input("Enter the tip percentage you would like to give (e.g., 10, 12, 15): "));
num_people  = int(input("Enter the number of people to split the bill: "))


tip_value= bill_amount * tip_percentage / 100
 

total_bill = bill_amount + tip_value

amount_per_person=total_bill / num_people

print("Total bill with tip is: $", total_bill)

print("Each person should pay: $", amount_per_person)
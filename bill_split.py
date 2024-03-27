#If the bill was $150.00, split between 5 people, with 12% tip. 

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people are splitting the bill? "))
tip_percent = tip/100
tip_amt = bill*tip_percent
bill_tip = bill + tip_amt
split = bill_tip / people
split = round(split, 2)
split = "{:.2f}".format(split)
print(f"Each person should pay ${split}")

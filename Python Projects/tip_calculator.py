print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("what percentage tip you would like to give? 10, 12 or 15? "))
tip_percentage = round(tip_percentage / 100,2)
people = int(input("How many people to split the bill? "))
total_bill = round(bill * (1 + tip_percentage),2)
pay = total_bill / people
print(f"Each person should pay: ${pay}")
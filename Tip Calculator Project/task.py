#Tip Calculator Project
print("Welcome to the tip calculator:")
bill=float(input("What was the total bill: "))
tip=int(input("What percentage tip would you like to give: "))
people=int(input("How many people to split the bill: "))
tip_percentage=tip/100
bill_tip=bill*tip_percentage
total_bill=bill+bill_tip
split=total_bill/people
formated_split=f"{split:.2f}"
print("Each person should pay:  ",formated_split)

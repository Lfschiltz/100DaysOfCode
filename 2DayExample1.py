#my version
print("Welcome to the tip calculator!")
tlbill = float(input(f"What was the total bill? "))
tenP = float(tlbill * 1.10)
twelP = float(tlbill * 1.12)
fiftnP = float(tlbill * 1.15)
tip = float(input(f"How much tip would you like to give? 10, 12, or 15? "))
if tip == 10:
    total = tenP
elif tip == 12:
    total = twelP
elif tip == 15:
    total = fiftnP
else:
    print("Must be a 10, 12, or 15 tip ")
numOfPpl = float(input("How many people to split the bill? "))
ttl = total / numOfPpl
print("Each person should pay: $",ttl)

#Angela's version
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

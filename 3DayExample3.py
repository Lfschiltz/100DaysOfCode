#My code
print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")
if size == "S":
    totalBill = 15
if size == "M":
    totalBill = 20
if size == "L":
    totalBill = 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        totalBill += 2
    else:
        totalBill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    totalBill += 1
print(f"Your final bill is ${totalBill}")

#Angela's code
print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
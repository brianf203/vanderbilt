# STEP 1

price = float(input("What is the unit price (in USD) of a single desk? "))
width = int(input ("What is the width (in feet) of the classroom? "))
length = int(input ("What is the length (in feet) of the classroom? "))

area = width * length
desks = area // 25

print("Room Area:", area, "sqft")
print("Number of desks needed:", desks)

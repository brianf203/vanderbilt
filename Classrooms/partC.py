# STEP 3

# CLASSROOM 1

print("CLASSROOM #1")
priceOne = float(input("What is the unit price (in USD) of a single desk? "))
widthOne = int(input ("What is the width (in feet) of the classroom? "))
lengthOne = int(input ("What is the length (in feet) of the classroom? "))

areaOne = widthOne * lengthOne
desksOne = areaOne // 25
priceOne = desksOne * 250
laborOne = desksOne * 5.5
taxOne = (priceOne + laborOne) * 0.0925
totalOne = priceOne + round(laborOne, 2) + round(taxOne, 2)

print("\nClassroom Order #1 Summary:")
print("Room area:", areaOne, "sqft")
print("Desk price: ${:.2f}".format(priceOne))
print("Labor cost: ${:.2f}".format(laborOne))
print("Sales tax: ${:.2f}".format(taxOne))
print("Total cost: ${:.2f}".format(totalOne))

# CLASSROOM 2

print("\nCLASSROOM #2")
priceTwo = float(input("What is the unit price (in USD) of a single desk? "))
widthTwo = int(input ("What is the width (in feet) of the classroom? "))
lengthTwo = int(input ("What is the length (in feet) of the classroom? "))

areaTwo = widthTwo * lengthTwo
desksTwo = areaTwo // 25
priceTwo = desksTwo * 200
laborTwo = desksTwo * 5.5
taxTwo = (priceTwo + laborTwo) * 0.0925
totalTwo = priceTwo + round(laborTwo, 2) + round(taxTwo, 2)

print("\nClassroom Order #2 Summary:")
print("Room area:", areaTwo, "sqft")
print("Desk price: ${:.2f}".format(priceTwo))
print("Labor cost: ${:.2f}".format(laborTwo))
print("Sales tax: ${:.2f}".format(taxTwo))
print("Total cost: ${:.2f}".format(totalTwo))

print("\nTotal cost for two classrooms: ${:.2f}".format(totalOne + totalTwo))

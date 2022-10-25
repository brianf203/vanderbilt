# PART B STEP 1

juice = float(input("What is the amount of lemon juice (in cups) needed: "))
water = float(input ("What is the amount of water (in cups) needed: "))
sugar = float(input ("What is the amount of sugar (in cups) needed: "))
teacups = float(input("How many tea cups does this recipe make? "))

print("Lemon tea ingredients - yields {:.2f}".format(teacups) + " cups.")
print("Lemon juice needed: {:.2f} ".format(juice) + " cup(s)")
print("Water needed: {:.2f}".format(water) + " cup(s)")
print("Sugar needed: {:.2f}".format(sugar) + " cup(s)")

# PART B STEP 2

cups = float(input("\nHow many cups would you like to make? "))
x = cups / teacups

print("Lemon tea ingredients - yields {:.2f}".format(cups) + " cups.")
print("Lemon juice needed: {:.2f} ".format(juice * x) + " cup(s)")
print("Water needed: {:.2f}".format(water * x) + " cup(s)")
print("Sugar needed: {:.2f}".format(sugar * x) + " cup(s)")

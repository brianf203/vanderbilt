# MIDTERM

lower = int(input("What is your value of X?: "))
upper = int(input("What is your value of Y?: "))

numbers = []

for i in range(lower, upper + 1):
    if i % 2 == 1:
        numbers.append(i)
    
print(numbers)

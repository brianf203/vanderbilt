# PART B

month = input("Enter month: ")
day = int(input("Enter day: "))

if month == "March" and 19 < day < 32 or month == "April" and 0 < day < 31 or month == "May" and 0 < day < 32 or month == "June" and 0 < day < 21:
    print ("\n" + month, day, "is a day in Spring")
elif month == "June" and 20 < day < 31 or month == "July" and 0 < day < 32 or month == "August" and 0 < day < 32 or month == "September" and 0 < day < 22:
    print ("\n" + month, day, "is a day in Summer")
elif month == "September" and 21 < day < 31 or month == "October" and 0 < day < 32 or month == "November" and 0 < day < 31 or month == "December" and 0 < day < 21:
    print ("\n" + month, day, "is a day in Autumn")
elif month == "December" and 20 < day < 32 or month == "Janurary" and 0 < day < 32 or month == "February" and 0 < day < 30 or month == "March" and 0 < day < 20:
    print ("\n" + month, day, "is a day in Winter")
else:
    print("\nInvalid date, season cannot be determined")

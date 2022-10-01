# MAIN

BABY = [(3, 38), (35, 38), (50, 36)]

for i in range(3):

	if BABY[i][0] <= 3 and 35.8 < BABY[i][1] <= 37.4 or 3 < BABY[i][0] <= 36 and 35.4 < BABY[i][1] <= 37.6 or BABY[i][0] > 36 and 35.4 < BABY[i][1] <= 37.7:
		print("Baby", str(i) + ":", "Normal temperature")

	elif 3 < BABY[i][0] <= 36 and 37.6 < BABY[i][1] <= 38.5 or BABY[i][0] > 36 and 37.7 < BABY[i][1] <= 39.4:
		print("Baby", str(i) + ":", "Moderate fever")

	else:
		print("Baby", str(i) + ":", "High fever")

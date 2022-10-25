# PART A

ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
NAME = "OLIVIA HARPER"
ALPHABETS_LIST = []
KEY = 3

print("Give a Key (1-10):", KEY, "\nNAME******")

for i in range(len(NAME)):
    print(f'{NAME[i]}{"--"}{i}')
    
print("KEY = 3", "\n**********", "\nALPHABETS***", "\nChar---i---i+KEY")

for i in range(len(ALPHABETS)):
    print(f'{ALPHABETS[i]}{"------"}{i}{"----"}{i + KEY}')
    ALPHABETS_LIST.append(ALPHABETS[i])
    
print("**********")

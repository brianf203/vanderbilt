# PART B

ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
NAME = "OLIVIA HARPER"
ALPHABETS_LIST = []
KEY = 3
DNAME_LIST = []

for i in range(len(ALPHABETS)):
    ALPHABETS_LIST.append(ALPHABETS[i])

def secure_de_identification(original_name, fun_key = 0):
    for char in original_name:
    	shifted_index = (ALPHABETS_LIST.index(char) + fun_key) % 27
    	DNAME_LIST.append(shifted_index)
    return DNAME_LIST
    
DNAME_LIST = secure_de_identification(NAME, KEY)
print("***Secure DNAME_LIST***\n" + str(DNAME_LIST) + "\n***Secure DNAME INDEX***\n" + "".join(str(x) for x in DNAME_LIST) + "\n***Secure DNAME CHARACTERS***")

for integer in DNAME_LIST:
    print(ALPHABETS_LIST[integer], end = "")

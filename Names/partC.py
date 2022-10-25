# PART C

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

def secure_decoding(d_name, fun_key = 0):
    real_name = []
    for num in d_name:
        index = (num - fun_key) % 27
        real_name.append(ALPHABETS_LIST[index])
    return real_name

print(secure_decoding(DNAME_LIST, KEY))

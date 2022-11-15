# PART B

def clean_token(input_token):
    c_token = ""
    for i in input_token:
        if i not in ["+", "'", ","]: 
            c_token += i 
    return c_token

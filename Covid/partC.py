# PART C

file1 = open("covid_text.txt", "r")
all_rows = file1.readlines()

print(f'{"Country Name":<15}{"Total Cases":^15}{"Total Death":^15}{"New Death":^10}{"Population":^10}' + "\n" + "-" * 65)

def clean_token(input_token):
    c_token = ""
    for i in input_token:
        if i not in ["+", "'", ","]: 
            c_token += i 
    return c_token

for row in all_rows:
    row_list = []
    for i in row.split():
        row_list.append(clean_token(i))
    print(f'{row_list[0]:<15}{row_list[1]:^15}{row_list[3]:^15}{row_list[4]:^10}{row_list[13]:^10}')

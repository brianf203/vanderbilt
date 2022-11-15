# PART A

file1 = open("covid_text.txt", "r")
all_rows = file1.readlines()

print(f'{"Country Name":<15}{"Total Cases":^15}{"Total Death":^15}{"New Death":^10}{"Population":^10}' + "\n" + "-" * 65)

for row in all_rows:
    row_list = row.split()
    print(f'{row_list[0]:<15}{row_list[1]:^15}{row_list[3]:^15}{row_list[4]:^10}{row_list[13][:len(row_list[13]) - 3]:^10}')

# PART E

import math

file1 = open("covid_text.txt", "r")
all_rows = file1.readlines()

print(f'{"Country Name":<15}{"Total Cases(%)":^15}{"Total Death(%)":^15}{"New Death(%)":^10}{"Population(%)":^10}' + "\n" + "-" * 65)

def clean_token(input_token):
    c_token = ""
    for i in input_token:
        if i not in ["+", "'", ","]: 
            c_token += i 
    return c_token

countries = []
total_cases = []
total_death = []
new_death = []
population = []

for row in all_rows:
    row_list = []
    for i in row.split():
        row_list.append(int(clean_token(i))) if clean_token(i).isnumeric() else row_list.append(clean_token(i))
    countries.append(row_list[0])
    total_cases.append(row_list[1])
    total_death.append(row_list[3])
    new_death.append(row_list[4])
    population.append(row_list[13])

for i in range(len(all_rows)):
    print(f'{countries[i]:<15}{math.ceil((total_cases[i] * 100) / sum(total_cases)):^15}{math.ceil((total_death[i] * 100) / sum(total_death)):^15}{math.ceil((new_death[i] * 100) / sum(new_death)):^10}{math.ceil((population[i] * 100) / sum(population)):^10}')

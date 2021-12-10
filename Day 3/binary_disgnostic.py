import pandas as pd
import numpy as np
from statistics import mode

#Read in Data
with open(r"C:\Users\Cherry\Desktop\Programming\Advent_Of_Code\Day 3\sample_data.txt", mode='rb') as file:
    data = file.read()

file.close()
data_str = str(data)
str_split = data_str[2:-6].split("\\r\\n")


# Define Functions
def get_nth_mode(num_list, n):
    nth_bit = [int(num[n-1]) for num in num_list]
    try:
        return mode(nth_bit)
    except:
        return 1


# Excute -Oxygen Generator Ratng
index = 0
remainder = str_split

while len(remainder) > 1:
    mode_val = get_nth_mode(remainder, index+1)

    filter_list = []
    for num in remainder:
        if int(num[index]) == mode_val:
            filter_list.append(num)

    remainder = filter_list
    index += 1

og_rating = remainder

# Excute CO2 scrubber Rating
index = 0
remainder = str_split

while len(remainder) > 1:
    mode_val = get_nth_mode(remainder, index+1)
    mode_val_invert = (mode_val+1) % 2

    filter_list = []
    for num in remainder:
        if int(num[index]) == mode_val_invert:
            filter_list.append(num)

    remainder = filter_list
    index += 1

CO2_rating = remainder

print('Oxygen Generator Rating: ', int(og_rating[0], 2))
print('CO2 scrubber Rating: ', int(CO2_rating[0], 2))
print('AOC Answer: ', int(og_rating[0], 2)*int(CO2_rating[0], 2))

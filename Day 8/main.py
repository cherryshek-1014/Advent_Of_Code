from collections import defaultdict
from os import dup
from decoder import run_decoder

with open(r'test_data.txt') as file:
    data = [line.rstrip() for line in file]

"""
# Part One 
"""


def count_unique_vals(output: list):
    result = output.split()
    num_val = 0
    for val in result:
        if len(val) in (2, 4, 3, 7):
            num_val += 1
    return num_val

# unqiue segement val 1,4,7,8


def get_total_unique_vals(data):
    total_unique_val = 0
    for entry in data:
        entry_split = entry.split(' | ')
        entry_pattern = entry_split[0]
        entry_output = entry_split[1]
        total_unique_val += count_unique_vals(entry_output)
    return (total_unique_val)


"""
Part Two 
"""
print('part1: {}'.format(get_total_unique_vals(data)))

total = 0
for signal in data:
    decode = run_decoder(signal)
    convert_to_num = int(''.join(map(str, decode)))
    total += convert_to_num

print(total)

import pandas as pd
import re
filename = 'input.txt'
# filename = 'input_small2.txt'

with open(filename, 'r') as file:
    input_string = file.read()

lines = input_string.split('\n')[0:-1]

str_digits = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
int_digits = ['0','1','2','3','4','5','6','7','8','9']

def find_digits(line, include_str_digits):
    # format is {location: digit}
    locs = dict()
    for d in int_digits:
        locs = locs | {match.start(): d for match in re.finditer(d, line)}
    if include_str_digits:
        for k, v in str_digits.items():
            locs = locs | {match.start(): v for match in re.finditer(k, line)}

    # Get digit from max location
    last = locs[max(locs.keys())]

    # Get digit from min location
    first = locs[min(locs.keys())]

    return first+last

# Part 1
r = [int(find_digits(line, include_str_digits=False)) for line in lines]
print('Part 1:', sum(r))

# Part 2
r = [int(find_digits(line, include_str_digits=True)) for line in lines]
print('Part 2:', sum(r))

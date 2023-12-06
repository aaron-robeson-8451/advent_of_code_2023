import pandas as pd
import re
import math
filename = 'input.txt'
# filename = 'input_small.txt'

with open(filename, 'r') as file:
    input_string = file.read()

lines = input_string.split('\n')[0:-1]

# Part 1
def points_of_number(xstart, xstop, y):
    points = [(y,x) for x in range(xstart, xstop+1)]
    return points

def perimiter_of_number(xstart, xstop, y):
    above = [(y-1, x) for x in range(xstart-1, xstop+2)]
    adjacent = [(y, x) for x in [xstart-1, xstop+1]]
    below = [(y+1, x) for x in range(xstart-1, xstop+2)]
    perimiter = above + adjacent + below
    return perimiter

def remove_outside_points(points, lines):
    # Remove any numbers that are not in the grid
    y_min = 0
    y_max = len(lines)-1
    x_min = 0
    x_max = len(lines[0])-1
    points = [point for point in points if point[0] >= y_min and point[0] <= y_max and point[1] >= x_min and point[1] <= x_max]
    return points

# 1) Find all numbers x/y corrdinates
# numbers = [{"number": 143, "xstart": 2, "xstop": 4, "y": 0, "points": [(0,0),... ], "perimiter_points": [(0,0), ...]}, ...]
numbers = []
for y, line in enumerate(lines):
    nums = re.finditer(r'(\d+)', line)
    r = [{'number': num.group(), 'xstart': num.span()[0], 'xstop': num.span()[1]-1, 'y': y} for num in nums]
    if r:
        numbers += r

# Add points and perimiter points to numbers
for num in numbers:
    points = points_of_number(num['xstart'], num['xstop'], num['y'])
    num['points'] = remove_outside_points(points, lines)
    perimiter = perimiter_of_number(num['xstart'], num['xstop'], num['y'])
    num['perimiter_points'] = remove_outside_points(perimiter, lines)

# 2) For each number check if it is adjacent to a symbol
number_sum = 0
for num in numbers:
    points_to_check = num['perimiter_points']
    # Check all points for symbols
    for y,x in points_to_check:
        if lines[y][x] not in ['1','2','3','4','5','6','7','8','9','0','.']:
            # We are adjacent to a symbol, count the number and stop checking
            number_sum += int(num['number'])
            break

print('Part 1:', number_sum)


# Part 2
# 2) Find all * x/y corrdinates
# stars = [{"x": 2, "y": 0, "points": [(2,0)], "perimiter_points": [(0,0), ...]}, ...]
stars = []
for y, line in enumerate(lines):
    stars += [{'x': x, 'y': y} for x, char in enumerate(line) if char == '*']
# add points and perimiter points to stars
for star in stars:
    points = [(star['y'], star['x'])]
    star['points'] = remove_outside_points(points, lines)
    perimiter = perimiter_of_number(star['x'], star['x'], star['y'])
    star['perimiter_points'] = remove_outside_points(perimiter, lines)

# 3) For each star find the numbers adjacent to it, if there are exactly two multiply them together
# def get_numbers_for_point(point, numbers):


for star in stars:
    # Check all perimiter points for numbers
    star_perimiter = star['perimiter_points']
    adjacent_numbers = []
    for num in numbers:
        for point in star_perimiter:
            if point in num['points']:
                adjacent_numbers.append(int(num['number']))
                break
    star['adjacent_numbers'] = adjacent_numbers

    
part2_total = 0
for star in stars:
    adjacent_numbers = star['adjacent_numbers']
    if len(adjacent_numbers) == 2:
        part2_total += math.prod(adjacent_numbers)

print('Part 2:', part2_total)

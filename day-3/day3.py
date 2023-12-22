# day3.py

import re

file = open('input.txt', 'r')
component_map = []
line_idx = 0
for line in file:
    component_map.append([])
    for char in line:
        component_map[line_idx].append([])
    line_idx += 1
file.close()


# Returns a list of matches with the data format of
# [x, y, length, string]
# By default, it searches for numbers
def find_symbols(file, regex="\d+"):
    file.seek(0)
    numbers = []
    line_idx = 0
    for line in file:
        matches = re.finditer(regex, line)
        for match in matches:
            x = match.start()
            y = line_idx
            length = match.end() - match.start()
            string = match[0]
            numbers.append([x, y, length, string])
        line_idx += 1
    return numbers


def check_validity(file, numbers):
    file.seek(0)
    symbol_regex = "[^\d.]" # anything that isn't a digit or a period
    valid_numbers = []
    grid = file.read().split("\n")[:-1]

    for num in numbers:
        valid = False
        num_x = num[0]
        num_y = num[1]
        num_size = num[2]
        num_value = num[3]
        # Boundary conditions
        if num_y > 0:
            for x in range(num_x, num_x + num_size):
                if re.match(symbol_regex, grid[num_y-1][x]):
                    component_map[num_y-1][x].append(num_value)
                    valid = True
        if num_y < len(grid)-2:
            for x in range(num_x, num_x + num_size):
                if re.match(symbol_regex, grid[num_y+1][x]):
                    component_map[num_y+1][x].append(num_value)
                    valid = True
        if num_x > 0:
            if re.match(symbol_regex, grid[num_y][num_x-1]):
                component_map[num_y][num_x-1].append(num_value)
                valid = True
        if num_x < len(grid[0])-1-num_size:
            if re.match(symbol_regex, grid[num_y][num_x+num_size]):
                component_map[num_y][num_x+num_size].append(num_value)
                valid = True

        # Diagonals
        if num_y > 0 and num_x > 0:
            char = grid[num_y-1][num_x-1]
            if re.match(symbol_regex, char):
                component_map[num_y-1][num_x-1].append(num_value)
                valid = True
        if num_y > 0 and num_x < len(grid[0])-1-num_size:
            char = grid[num_y-1][num_x+num_size]
            if re.match(symbol_regex, char):
                component_map[num_y-1][num_x+num_size].append(num_value)
                valid = True
        if num_y < len(grid)-2 and num_x > 0:
            char = grid[num_y+1][num_x-1]
            if re.match(symbol_regex, char):
                component_map[num_y+1][num_x-1].append(num_value)
                valid = True
        if num_y < len(grid)-2 and num_x < len(grid[0])-1-num_size:
            char = grid[num_y+1][num_x+num_size]
            if re.match(symbol_regex, char):
                component_map[num_y+1][num_x+num_size].append(num_value)
                valid = True

        if valid: valid_numbers.append(num)
    return valid_numbers


def sum_valid_numbers(numbers):
    sum = 0
    for num in numbers:
        sum += int(num[3])
    return sum

# # example 1: sum of all the 'actual' part numbers. Should be 4361
# file = open('example.txt', 'r')
# numbers = find_numbers(file)
# valid_numbers = check_validity(file, numbers)
# print(sum_valid_numbers(valid_numbers))
# file.close()

# # part 1: using the input data
# # answer was 525119
# file = open('input.txt', 'r')
# numbers = find_numbers(file)
# valid_numbers = check_validity(file, numbers)
# print(sum_valid_numbers(valid_numbers))
# file.close()

# part 2: get the sum of the products of each pair connected to a gear '*'
# Here's the thing - each number is only ever touching one symbol, or none,
# and if its a 'gear', then the gear might be connected to 1,2,3, (or 4?) numbers
# So, I'll make a 'component map', which overlays the map, and I can
# store the numbers connected to each component, then look at what numbers are on each gear

file = open('input.txt', 'r')
numbers = find_symbols(file)
valid_numbers = check_validity(file, numbers)
gears = find_symbols(file, "\*")
sum = 0
for gear in gears:
    related_components = component_map[gear[1]][gear[0]]
    has_gear_ratio = len(related_components) == 2
    if has_gear_ratio:
        sum += int(related_components[0]) * int(related_components[1])
print(sum)
file.close()

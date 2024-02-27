# day12.py

import re

def parse(filename):
    file = open(filename, 'r')
    data = []
    for line in file:
        puzzle, key = re.split(' ', line.strip("\n"))
        key = re.split(',', key)
        key = list(map(int, key))
        data.append([puzzle, key])
    file.close()
    return data


# Some of my options:
# - Come up with every single possibility, and see if it fits in the hint, sum them up
# TODO I'll need to use Dynamic Programming or Deterministic Finite Automata to solve
def part1(data):
    for line in data:
        print(line)

    sum = 0
    for puzzle in data:
        print("\n", puzzle)
        string = puzzle[0]
        keys = puzzle[1]
        regex = "^[.]*"
        for i in range(len(keys)):
            for j in range(keys[i]):
                regex += "#"
            if i != len(keys)-1:
                regex += "[.]+"
        regex += "[.]*$"
        print(regex)
        length = len(puzzle[0])
        sum += get_all_solutions(string, regex)

    return sum


# Recursive function that counts and returns the number of possible solutions
def get_all_solutions(string, regex):
    solutions = 0
    for i in range(len(string)):
        if string[i] != '?':
            continue
        new_string = string[:i] + "#" + string[i+1:]
        solutions += solutions + get_all_solutions(new_string, regex)
        new_string = string[:i] + "." + string[i+1:]
        return solutions + get_all_solutions(new_string, regex)

    if re.match(regex, string):
        return 1
    return 0

# Part 1 example 1 should return 21
#print(part1(parse("example.txt")))
# Part 1 answer should be 7753, and takes about 20 seconds with the recursive method
#print(part1(parse("input.txt")))


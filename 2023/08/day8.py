# day8.py

import time
import re

def parse(filename):
    file = open(filename, 'r')
    contents = file.read().splitlines()
    instructions = list(contents[0])
    maps_raw = contents[2:]
    maps = {}
    for line in maps_raw:
        matches = re.findall("\w{3}", line)
        maps[matches[0]] = (matches[1], matches[2])
    file.close()
    return instructions, maps

def part1(instructions, maps):
    key = 'AAA'
    steps = 0
    while key != 'ZZZ':
        if instructions[0] == 'L':
            key = maps[key][0]
        else:
            key = maps[key][1]
        instructions.append(instructions.pop(0))
        steps += 1
    return steps

# example 1 answer is 2 steps, example 2 answer is 6 steps
instructions, maps = parse("example1.txt")
part1(instructions, maps)
instructions, maps = parse("example2.txt")
part1(instructions, maps)

# part 1: answer is 17141
instructions, maps = parse("input.txt")
part1(instructions, maps)


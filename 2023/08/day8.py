# day8.py

import time
import re
from math import lcm

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
# instructions, maps = parse("example1.txt")
# part1(instructions, maps)
# instructions, maps = parse("example2.txt")
# part1(instructions, maps)

# part 1: answer is 17141
instructions, maps = parse("input.txt")
print(part1(instructions, maps))

# part 2: example 3 answer is 6
# My input has 6 nodes that end with A and 6 nodes that end with Z
# How many steps until I'm ONLY on nodes that end with Z?
# I can iterate until it occurs, or I can calculate the lowest common multiple of each loop
# I'm going to iterate, because there are too many unknown possibilities,
# like each loop could pass through multiple **Z nodes, but I don't necessarily know if that's the case
# Nevermind, I read that this is indeed a LCM problem, and that it's unfeasible to do brute-force.
# Looks like each **A key only ever passes by one single **Z key, so this is an easy LCM problem
# Example, Node AAA repeats every 17141 steps, node XQA repeats with NNZ every 16579 steps
# Note that the **Z node is always found at the end of the instruction set,
# so all key periods have this as a common factor (281 characters), example AAA repeats every
# 17141 steps, which is 61 times the instruction set, and XQA repeats every 16579, which is
# 59 times the instruction set
# part 2 answer is 10818234074807
def part2(filename):
    file = open(filename, 'r')
    contents = file.read().splitlines()
    instructions = list(contents[0])
    for idx in range(len(instructions)):
        if instructions[idx] == 'L':
            instructions[idx] = 0
        else:
            instructions[idx] = 1
    maps_raw = contents[2:]
    maps = {}
    starting_keys = []
    for line in maps_raw:
        matches = re.findall("\w{3}", line)
        maps[matches[0]] = (matches[1], matches[2])
        if matches[0][2] == 'A':
            starting_keys.append(matches[0])
    file.close()

    periods = []
    for key in starting_keys:
        periods.append(get_period(key, instructions, maps))
    print(periods)

    return lcm(*periods)
    # steps = 0
    # while not all_ending_in_z(keys):
    #     for idx in range(len(keys)):
    #         keys[idx] = maps[keys[idx]][instructions[0]]
    #     instructions.append(instructions.pop(0))
    #     steps += 1
    # return steps

# def all_ending_in_z(keys):
#     for key in keys:
#         if key[2] != 'Z': return False
#     return True

# Returns the number of steps that a key takes before it repeats
def get_period(key, instructions, maps):
    steps = 0
    while key[2] != 'Z':
        key = maps[key][instructions[0]]
        instructions.append(instructions.pop(0))
        steps += 1
    return steps

print(part2("example3.txt"))

print("running on input.txt ...")
start = time.time()
print(part2("input.txt"))
end = time.time()
print(end - start)


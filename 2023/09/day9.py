# day9.py
# Need to get the next number in each series, and add them together

import re

# Split all lines into series of integers
def parse(filename):
    file = open(filename, 'r')
    histories = file.read().splitlines()
    for idx in range(len(histories)):
        histories[idx] = list(map(int, histories[idx].split()))
    file.close()
    return histories
    
def part1(data):
    sum = 0
    for series in data:
        # print("\nNEW SERIES", series)
        sum += get_next_number(series)
    return sum

# Recursive function that takes a series (list), and return the next number in the series
def get_next_number(series):
    # print("Getting next number in series", series)
    deltas = []
    for i in range(1, len(series)):
        deltas.append(series[i]-series[i-1])
    # print("Deltas of this series are", deltas)

    # Base case of the series being linear (deltas are all 0):
    if not any(deltas):
        # print("returning", series[-1])
        return series[-1]
    next_num = series[-1] + get_next_number(deltas)
    # print("Collapsing with", next_num)
    return next_num

def part2(data):
    sum = 0
    for series in data:
        # print("\nNEW SERIES", series)
        sum += get_prev_number(series)
    return sum

# Recursive function that takes a series (list), and return the previous number in the series
def get_prev_number(series):
    # print("Getting previous number in series", series)
    deltas = []
    for i in range(1, len(series)):
        deltas.append(series[i]-series[i-1])
    # print("Deltas of this series are", deltas)

    # Base case of the series being linear (deltas are all 0):
    if not any(deltas):
        # print("returning", series[0])
        return series[0]
    next_num = series[0] - get_prev_number(deltas)
    # print("Collapsing with", next_num)
    return next_num

    
# Example answer is 114
print("P1 example:", part1(parse("example.txt")))
# Part 1 answer is 1666172641
print("P1 answer: ", part1(parse("input.txt")))

# Part 2 example is 2
print("P2 example:", part2(parse("example.txt")))
# Part 2 answer is 933
print("P2 answer: ", part2(parse("input.txt")))

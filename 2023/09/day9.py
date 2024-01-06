# day9.py
# Need to get the next number in each series, and add them together

import re

def part1(filename):
    # Split all lines into series of integers
    file = open(filename, 'r')
    histories = file.read().splitlines()
    for idx in range(len(histories)):
        histories[idx] = list(map(int, histories[idx].split()))
    file.close()

    sum = 0
    for series in histories:
        print("\nNEW SERIES", series)
        sum += get_next_number(series)
    return sum

# Recursive function that takes a series (list), and return the next number in the series
def get_next_number(series):
    print("Getting next number in series", series)
    deltas = []
    for i in range(1, len(series)):
        deltas.append(series[i]-series[i-1])
    print("Deltas of this series are", deltas)

    # Base case of the series being linear (deltas are all 0):
    if not any(deltas):
        print("returning", series[-1])
        return series[-1]
    next_num = series[-1] + get_next_number(deltas)
    print("Collapsing with", next_num)
    return next_num

# Example answer is 114
print(part1("example.txt"))
# Part 1 answer is 1666172641
print(part1("input.txt"))

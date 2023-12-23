# day4.py

import re

# It doesn't look like the 'scratchcards' have a pattern to the
# numbers, so I don't think I can do better than checking every number
# against every winning number

file = open('example.txt', 'r')
example_data = file.read().split("\n")[:-1]
file = open('input.txt', 'r')
input_data = file.read().split("\n")[:-1]
file.close()


winning_numbers_regex = ": *(\d.*\d) \|"
playing_numbers_regex = "\| *(\d.*)$"


def get_numbers(data, regex):
    numbers = []
    for line in data:
        numbers.append(list(map(int, re.search(regex, line)[1].split())))
    return numbers

def get_num_matches(winning_numbers, playing_numbers):
    matches = []
    for game in range(len(winning_numbers)):
        num_matches = 0
        for wnum in winning_numbers[game]:
            for pnum in playing_numbers[game]:
                if wnum == pnum:
                    num_matches += 1
        matches.append(num_matches)
    return matches

def calc_points(matches):
    sum = 0
    for m in matches:
        if m > 0: sum += 2 ** (m-1)
    return sum

# # example: should be 13
# winners = get_numbers(example_data, winning_numbers_regex)
# numbers = get_numbers(example_data, playing_numbers_regex)
# matches = get_num_matches(winners, numbers)
# print(calc_points(matches))

# # part 1, answer is 25004
# winners = get_numbers(input_data, winning_numbers_regex)
# numbers = get_numbers(input_data, playing_numbers_regex)
# matches = get_num_matches(winners, numbers)
# print(calc_points(matches))

# part 2: wins explode by winning additional cards
# this will likely need recursion to solve
# TODO

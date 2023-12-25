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
# I tried recursion, but Python's recursion limit didn't like that,
# so I went back to a while-loop on a stack, which was actually simpler for this task
# It was taking too long, so I figure that the solution was to scratch them backwards,
# and cache the number of cards that each card wins
# answer is 14427616

# Returns the number of matches between two lists of numbers
def calc_matches(set1, set2):
    num_matches = 0
    for i in set1:
        for j in set2:
            if i == j:
                num_matches += 1
    return num_matches

# # Initial set is the list of cards, numbers, and the number of matches for each card
# def scratch_cards(card_stack, initial_set):
#     card_count = 0
#     while len(card_stack) > 0:
#         card = card_stack.pop(0)
#         card_count += 1
#         wins = initial_set[card-1][3]
#         for i in range(wins):
#             # Don't add cards beyond the possible set of cards
#             if card+i+1 <= len(initial_set):
#                 card_stack.append(card+1+i)
#     return card_count

# Take 2, going backward and caching the results
# Initial set is the list of cards, numbers, and the number of matches for each card
# Card stack needs to be reverse sorted for the caching to work
# Recursion would be very efficient for this, but I'm not doing it that way
def scratch_cards(card_stack, initial_set):
    while len(card_stack) > 0:
        card = card_stack.pop(0)
        card_worth = initial_set[card-1][4]
        wins = initial_set[card-1][3]
        # Start calculating a card's worth by counting itself
        if card_worth < 0:
            card_worth = 1
        for i in range(card+1, card+1+wins):
            # Don't add cards beyond the possible set of cards
            if i <= len(initial_set):
                # if the card has a calculated worth, already
                if initial_set[i-1][4] > -1:
                    card_worth += initial_set[i-1][4]
                else:
                    card_stack.append(i)
        initial_set[card-1][4] = card_worth
    card_count = 0
    for line in initial_set:
        card_count += line[4]
    return card_count

# Table of cards format:
# [ <card_number>, [<winning_numbers>], [<playing_numbers>], <number of wins>, <worth>]
# <worth> is initialised at -1 to show that it hasn't been calculated yet,
# it indicates how much a card is worth after scratching it and all decendant tickets

# winners = get_numbers(example_data, winning_numbers_regex)
# numbers = get_numbers(example_data, playing_numbers_regex)
winners = get_numbers(input_data, winning_numbers_regex)
numbers = get_numbers(input_data, playing_numbers_regex)
card_table = []
card_stack = []
num_cards = len(winners)
for i in range(num_cards):
    matches = calc_matches(winners[i], numbers[i])
    card_table.append([i+1, winners[i], numbers[i], matches, -1])
    card_stack.append(i+1)
card_stack.reverse()
print(num_cards, "cards to scratch, initially")
card_total = scratch_cards(card_stack, card_table)
print(card_total, "total cards in the end")
# for line in card_table:
#     print(line)


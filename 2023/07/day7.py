# day7.py

from functools import cmp_to_key, partial

CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

# Reads each hand in the file, and returns the data as a table:
# [ [<cards>, <bid>], ... ]
def parse(filename):
    file = open(filename, 'r')
    data = []
    for line in file:
        hand, bid = line.split()
        data.append([hand, int(bid)])
    file.close()
    return data

# A custom sorting function to compare two hands as per the "camel cards" rules
def compare_hands(a, b, part2=False):
    difference = calculate_hand(a[0], part2) - calculate_hand(b[0], part2)
    if difference < 0:
        return -1
    elif difference > 0:
        return 1
    elif difference == 0:
        for i in range(len(a[0])):
            if compare_values(a[0][i], b[0][i]) < 0:
                return -1
            elif compare_values(a[0][i], b[0][i]) > 0:
                return 1
    raise Exception("Hands must be different.")

# Custom compare function to compare two cards as per the "camel cards" rules
# Descending order of power: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2, 1
# All parameters must be strings
def compare_values(a, b):
    if CARD_VALUES[a] < CARD_VALUES[b]:
        return -1
    elif CARD_VALUES[a] > CARD_VALUES[b]:
        return 1
    return 0

# Returns a value for the type of hand held: 0, high-card; 1, one-pair; 2, two-pair; 3, three-of-a-kind;
# 4, full-house; 5, four-of-a-kind; 6, five-of-a-kind
# This can likely be improved with Enums?
def calculate_hand(hand, part2=False):
    card_counts = {}
    for c in hand:
        if c in card_counts:
            card_counts[c] += 1
        else:
            card_counts[c] = 1
    joker_count = 0
    if part2:
        if 'J' in card_counts:
            joker_count = card_counts['J']
            # If the joker count is 5, then the whole hand is jokers, and must be counted
            # as the lowest five-of-a-kind
            if joker_count < 5: del card_counts['J']
    sorted_counts = sorted(card_counts.items(), key=lambda card: card[1], reverse=True)
    if 0 < joker_count < 5:
        card_counts[sorted_counts[0][0]] += joker_count
        sorted_counts = sorted(card_counts.items(), key=lambda card: card[1], reverse=True)

    most = sorted_counts[0][1]
    second_most = 0
    if len(sorted_counts) >= 2: second_most = sorted_counts[1][1]
    if most == 5: return 6
    elif most == 4: return 5
    elif most == 3 and second_most == 2: return 4
    elif most == 3: return 3
    elif most == 2 and second_most == 2: return 2
    elif most == 2: return 1
    else: return 0

# Returns the "total winnings" of all the hands, which is their rank multiplied by their bid
# Takes an optional function, which serves as the comparison function to compare hands
def get_winnings(data, part2=False):
    if part2:
        CARD_VALUES['J'] = 1

    ranked_hands = sorted(data, key=cmp_to_key(partial(compare_hands, part2=part2)))
    
    # Calculate all the winnings
    winnings = 0
    rank = 1
    for hand in ranked_hands:
        winnings += hand[1] * rank
        rank += 1
    
    return winnings

# # example: answer is 6440
# data = parse("example.txt")
# print(get_winnings(data))

# # part 1: answer is 248113761
# # This problem is a sorting algorithm problem
# data = parse("input.txt")
# print(get_winnings(data))

# part 2 example: answer is 5905
# This problem is just a matter of changing the comparison function
# Jokers are now wild, but count as the lowest value when breaking ties
data = parse("example.txt")
print(get_winnings(data, part2=True))
# part 2 answer is 246285222
data = parse("input.txt")
print(get_winnings(data, part2=True))

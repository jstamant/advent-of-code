# day-1.py

import re
import pytest

def day1(input_file):
    sum = 0
    for line in input_file:
        first_num = re.search("\d", line)[0]
        last_num = re.search("\d\D*?$", line)[0][0]
        combined_num = first_num + last_num
        sum += int(combined_num)
    return sum


# Problem: if words overlap, they need to be properly figured out:
# 'twone' matches as 'one' for the last digit.
import regex # this third-party module supports overlapping matches
def day1_part2(input_file):
    sum = 0
    for line in input_file:
        matches = regex.findall("\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
        first_num = word_to_int(matches[0])
        last_num = word_to_int(matches.pop())
        combined_num = first_num + last_num
        sum += int(combined_num)
    return sum

# Converts a number as a word to a digit in a string ("one" -> "1")
# Does nothing to unrecognized strings
def word_to_int(string):
    match string:
        case 'one': return '1'
        case 'two': return '2'
        case 'three': return '3'
        case 'four': return '4'
        case 'five': return '5'
        case 'six': return '6'
        case 'seven': return '7'
        case 'eight': return '8'
        case 'nine': return '9'
    return string

print("Running...")
input = open('input', 'r')
print("Sum is:", day1_part2(input))
# should be 142 for part 1
# part 1 solution is 56465
# should be 281 for part 2
# part 2 solution is 55902
input.close()
print("Done!")

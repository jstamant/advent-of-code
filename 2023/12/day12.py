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


def unfold(data):
    new_data = [*data]
    for record in new_data:
        record[0] += ('?' + record[0]) * 4
        record[1] = record[1] * 5
    return new_data


# TODO I need to add memoization to optimize
# TODO or better: I need to operate by number of heads rather than recurse through them all
def part2(data):
    sum = 0
    for record in data:
        print(record[0])
        print(record[1])
        states = generate_states(record[1])
        possibilities = DFA(record[0], states).recurse()
        print(sum, "+", possibilities, "\n")
        sum += possibilities
    return sum


class DFA:
    def __init__(self, string, states, state=0, pos=0):
        self.string = string
        self.pos = pos
        self.state = state
        self.states = states
        self.successes = 0
        # print("New head with string", string, "and state", state)

    def recurse(self):
        for position in range(self.pos, len(self.string)):
            character = self.string[position]
            if character == '?':
                for char in ['.', '#']:
                    string = self.string[:position] + char + self.string[position+1:]
                    self.successes += DFA(string, self.states, self.state, position).recurse()
                return self.successes
            else:
                if character in self.states[self.state]:
                    self.state += self.states[self.state][character]
                else:
                    # print("terminating head", self.string, "that had successes x", self.successes)
                    return 0
        if self.state == len(self.states)-1:
            # print("successful head!", self.string)
            return 1
        else:
            return 0

def generate_states(keys):
    states = []
    states.append({'.': 0})
    for key in keys:
        for i in range(key):
            states[-1]['#'] = 1
            states.append({})
        states[-1]['.'] = 1
        states.append({'.': 0})
    states.pop()
    states[-1]['.'] = 0
    return states



# Part 1 example 1 should return 21
#print(part1(parse("example.txt")))
# Part 1 answer should be 7753, and takes about 20 seconds with the recursive method
#print(part1(parse("input.txt")))

# Part 2 example should return 525152
print(part2(unfold(parse("example.txt"))))
# Part 2 answer should return 280382734828319
print(part2(unfold(parse("input.txt"))))

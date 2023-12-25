# day2.py

import re
import math

# Parses puzzle data into an array
# [[ <game>, <red>, <green>, <blue>],
#  [ <game>, <red>, ...    , ...   ],
#  [ ...                           ]]
def parse_game(file):
    table = []
    for line in file:
        data = [0, 0, 0, 0]
        line = line[:-1] # get rid of the newline
        data[0] = int(re.match("Game (\d+): ", line).group(1))
        game = re.split('[:;] ', line)[1:]
        for hand in game:
            colors = re.split(', ', hand)
            for i in colors:
                color = re.search(' (.*)$', i).group(1)
                num = int(re.match('(\d+)', i).group(1))
                if color == 'red':   data[1] = max(data[1], num)
                if color == 'green': data[2] = max(data[2], num)
                if color == 'blue':  data[3] = max(data[3], num)
        table.append(data)
    return table

def check_games(table, rgb_max=[12, 13, 14]):
    possible_games = []
    print('Using', rgb_max, 'as the max colors')
    for game in table:
        print(game)
        game_possible = True
        for c in range(1,4):
            if game[c] > rgb_max[c-1]:
                game_possible = False
        if game_possible:
            possible_games.append(game[0])
    print('Possible games:', possible_games)
    return possible_games


# # example 1: sum of possible games if bag had 12 red cubes, 13 green cubes, and 14 blue cubes
# file = open('example.txt', 'r')
# table = parse_game(file)
# print(table)
# possible_games = check_games(table)
# print('Sum of possible game IDs:', sum(possible_games))
# file.close()

# # part 1: sum of possible games if bag had 12 red cubes, 13 green cubes, and 14 blue cubes
# # solution was 2727
# file = open('input.txt', 'r')
# table = parse_game(file)
# possible_games = check_games(table)
# print('Sum of possible game IDs:', sum(possible_games))
# file.close()

# part 2: sum of the products of the minimum amount of cubes for each game
# solution was 56580
file = open('input.txt', 'r')
table = parse_game(file)
running_sum = 0
for game in table:
    product = game[1] * game[2] * game[3]
    running_sum += product
print('"Sum of the power" of the input sets is:', running_sum)
file.close()

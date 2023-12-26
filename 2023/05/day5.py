# day5.py

import re

file = open('input.txt', 'r')
data = file.read()
file.close()

data = data.split("\n")

seed_pattern = "seeds: (\d.*)"
next_map_pattern = "map:"
map_pattern = "^(\d.*\d)$"

seeds = []
maps = []
map_number = -1
for line in data:
    m = re.match(seed_pattern, line)
    if m:
        seeds = m[1].split()
    if re.search(next_map_pattern, line):
        map_number += 1
        maps.append([])
    m = re.match(map_pattern, line)
    if m:
        map_line = m[1].split()
        maps[map_number].append(map_line)

for i in range(len(seeds)):
    seeds[i] = int(seeds[i])
for i in range(len(maps)):
    for j in range(len(maps[i])):
        for k in range(len(maps[i][j])):
            maps[i][j][k] = int(maps[i][j][k])


# I need to check each seed against the maps.

# I think the best approach would be to make a list of maps

# Takes a seed, puts it through all the maps, and returns the final mapped value
def translate_seed(seed, maps):
    idx = seed
    for map_set in maps:
        for map_line in map_set:
            dest_start = map_line[0]
            src_start = map_line[1]
            length = map_line[2]
            if src_start <= idx < src_start+length:
                new_idx = dest_start + (idx - src_start)
                idx = new_idx
                break
    return idx


# # example: lowest seed location should be 35
# # part 1: answer is 289863851
# lowest_location = -1
# for seed in seeds:
#     location = translate_seed(seed, maps)
#     if lowest_location == -1:
#         lowest_location = location
#     else:
#         lowest_location = min(location, lowest_location)
# print("lowest is", lowest_location)


# part 2: it's not individual seeds, it's a range of seeds
# Needs optimizaion in order to run. Checking every single seed is not feasible
# You need to cut out ranges
lowest_location = -1
for i in range(0, len(seeds)-1, 2):
    for seed in range(seeds[i], seeds[i]+seeds[i+1]):
        location = translate_seed(seed, maps)
        if lowest_location == -1:
            lowest_location = location
        else:
            lowest_location = min(location, lowest_location)
print("lowest is", lowest_location)

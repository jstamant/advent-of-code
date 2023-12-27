# day5.py

import re

# file = open('input.txt', 'r')
# data = file.read()
# file.close()

# data = data.split("\n")

# seed_pattern = "seeds: (\d.*)"
# next_map_pattern = "map:"
# map_pattern = "^(\d.*\d)$"

# seeds = []
# maps = []
# map_number = -1
# for line in data:
#     m = re.match(seed_pattern, line)
#     if m:
#         seeds = m[1].split()
#     if re.search(next_map_pattern, line):
#         map_number += 1
#         maps.append([])
#     m = re.match(map_pattern, line)
#     if m:
#         map_line = m[1].split()
#         maps[map_number].append(map_line)

# for i in range(len(seeds)):
#     seeds[i] = int(seeds[i])
# for i in range(len(maps)):
#     for j in range(len(maps[i])):
#         for k in range(len(maps[i][j])):
#             maps[i][j][k] = int(maps[i][j][k])


# I need to check each seed against the maps.

# I think the best approach would be to make a list of maps

# # Takes a seed, puts it through all the maps, and returns the final mapped value
# def translate_seed(seed, maps):
#     idx = seed
#     for map_set in maps:
#         for map_line in map_set:
#             dest_start = map_line[0]
#             src_start = map_line[1]
#             length = map_line[2]
#             if src_start <= idx < src_start+length:
#                 new_idx = dest_start + (idx - src_start)
#                 idx = new_idx
#                 break
#     return idx


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

# # Needs optimizaion in order to run. Checking every single seed is not feasible
# # Not feasible, needs optimizing
# lowest_location = -1
# for i in range(0, len(seeds)-1, 2):
#     for seed in range(seeds[i], seeds[i]+seeds[i+1]):
#         location = translate_seed(seed, maps)
#         if lowest_location == -1:
#             lowest_location = location
#         else:
#             lowest_location = min(location, lowest_location)
# print("lowest is", lowest_location)



# Next try - using ranges of seeds instead of individual seeds

def parse(filename):
    file = open(filename, 'r')
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

    # Generate ranges of numbers
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i]+seeds[i+1]])
    # Generate map ranges instead of showing them by offset
    # [ <source_start>, <source_end(exclusive)>, <dest_start>, <dest_end(exclusif)> ]
    maps_ranges = []
    for map_i in range(len(maps)):
        maps_ranges.append([])
        for mapline in range(len(maps[map_i])):
            maps_ranges[map_i].append([
                maps[map_i][mapline][1],
                maps[map_i][mapline][1] + maps[map_i][mapline][2],
                maps[map_i][mapline][0],
                maps[map_i][mapline][0] + maps[map_i][mapline][2]])
    return seed_ranges, maps_ranges

def sort_maps(maps_list):
    sorted_maps = []
    for each_map in maps:
        sorted_maps.append(sorted(each_map))
    return sorted_maps

seeds, maps = parse("input.txt")
print(seeds)
print(maps)
# sort the seed ranges in ascending order
# seeds = sort_indexes(seeds)
seeds = sorted(seeds)
print(sorted(seeds))

# sort the maps in ascending order
maps = sort_maps(maps)
print(maps)


# Determines if two numerical ranges coincide
# region format: [ <start>, <end(exclusif)> , ...possibly more indexes ]
# Returns [] if no collision is found, or
# Returns a range [ start, end ] where the collision occurs
def collides(range1, range2):
    # Sort regions by which one has the lowest starting point
    # So that r1 always has the lower starting point
    r1, r2 = [*range1], [*range2]
    if range1[0] > range2[0]: r1, r2 = r2, r1
    r1_start, r1_end = r1[0], r1[1]
    r2_start, r2_end = r2[0], r2[1]
    if r1_end <= r2_start:
        return []
    if r1_end < r2_end:
        return [r2_start, r1_end]
    else:
        return [r2_start, r2_end]

# Use recursion to apply each map, one at a time, and return the sorted list of indexes
def apply_maps(indexes, maps):
    if len(maps) == 0:
        return indexes
    print("Apply maps called with:", indexes)
    print("and maps[0]:", maps[0])

    new_indexes = []
    while len(indexes) > 0:
        print("\nSEED RANGE:", indexes[0])
        start = indexes[0][0]
        end = indexes[0][1]
        collision = False

        for line in maps[0]:
            map_start = line[0]
            map_end = line[1]
            print("Map line:", line)
            collision_range = []
            non_collision_range = []
            if end <= map_start or map_end <= start:
                print("no collision, checking next map line")
            elif map_start <= start and end <= map_end:
                print("completely overlapped")
                collision = True
                collision_range = [start, end]
            elif start < map_start and end <= map_end:
                print("partially overlapped")
                collision = True
                collision_range = [map_start, end]
                non_collision_range = [start, map_start]
            elif map_start < start and map_end <= end:
                print("partially overlapped")
                collision = True
                collision_range = [start, map_end]
                non_collision_range = [map_end, end]
            if collision_range:
                print("collision range", collision_range)
                print("non-colliding range", non_collision_range)
                mapping_delta = line[2] - line[0]
                print("offset is", mapping_delta)
                new_indexes.append([collision_range[0]+mapping_delta, collision_range[1]+mapping_delta])
                if non_collision_range:
                    indexes.append([non_collision_range[0], non_collision_range[1]])
                break
        if not collision:
            print("No collision on range", [start, end], "- forwarding index")
            new_indexes.append([start, end])
        indexes = indexes[1:]

    print("NEW INDEXES:", sorted(new_indexes))
    print("Remaining maps:", maps[1:])
    return apply_maps(sorted(new_indexes), maps[1:])

# Answer for part 2 is 60568880? Needs to be submitted
# TODO remove all print statements
def day5_part2(seeds, maps):
    lowest = apply_maps(seeds, maps)[0]
    return lowest

print(day5_part2(seeds, maps))

# day11.py

def parse(filename):
    file = open(filename, 'r')
    print(filename + ":")
    data = []
    for line in file:
        data.append(list(line)[:-1])
    file.close()
    return data

# I solve this challenge by making a map of distances.
# Expanded space has a larger number in it, which equates to adding more distance
def solve(data, factor=2):
    print("factor of", factor)
    # First, I need to "expand" the map, which inserts the factor number in the space
    map = []
    for row in range(len(data)):
        map.append([])
        empty = False
        if is_empty(data[row]):
            empty = True
        for col in range(len(data[row])):
            if empty:
                element = factor
            else:
                element = 1 if data[row][col] == '.' else '#'
            map[row].append(element)
    for col in reversed(range(len(map[0]))):
        empty = True
        for row in range(len(map)):
            if map[row][col] == '#':
                empty = False
        if empty:
            expand_column(map, col, factor)

    # List all galaxies
    galaxies = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '#':
                galaxies.append((x, y))
    # Then, sum all the shortest paths, which is just the x and y distance
    sum = 0
    for galaxy in galaxies:
        for destination in galaxies:
            distance = calculate_distance(galaxy, destination, map)
            sum += distance
    return sum

# Returns true if all elements in the list are '.'
def is_empty(line):
    for element in line:
        if element != '.': return False
    return True

def expand_column(map, index, factor):
    for row in range(len(map)):
        map[row][index] = factor

def calculate_distance(src, dest, map):
    if src == dest: return 0
    dx = 0
    dy = 0
    for col in range(src[0], dest[0]):
        cell = map[src[1]][col+1]
        value = cell if cell != '#' else 1
        dx += value
    for row in range(src[1], dest[1]):
        cell = map[row][dest[0]]
        value = cell if cell != '#' else 1
        dy += value
    return dx + dy

# Example 1 should be 374
print(solve(parse("example1.txt")))
# Part 1 answer is 9805264
#print(solve(parse("input.txt")))

# Example 1 using part 2 rules should be 1030 for an expansion factor of 10, and 8410 for 100
print(solve(parse("example1.txt"), 10))
print(solve(parse("example1.txt"), 100))
# Part 2 answer is 779032247216
print(solve(parse("input.txt"), 1000000))

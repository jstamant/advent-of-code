# day11.py

def parse(filename):
    file = open(filename, 'r')
    print(filename + ":")
    data = []
    for line in file:
        data.append(list(line)[:-1])
    file.close()
    return data

def part1(data):
    # First, I need to "expand" the map, which is doubling any empty lines
    map = []
    # Add double empty rows
    for line in data:
        map.append([*line])
        if is_empty(line):
            map.append([*line])
    for col in reversed(range(len(map[0]))):
        empty = True
        for element in range(len(map)):
            if map[element][col] != '.':
                empty = False
        if empty:
            copy_column(map, col)

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
            distance = abs(destination[0]-galaxy[0]) + abs(destination[1]-galaxy[1])
            sum += distance
    return sum/2

# Returns true if all elements in the list are '.'
def is_empty(line):
    for element in line:
        if element != '.': return False
    return True

def copy_column(map, index):
    for row in range(len(map)):
        map[row].insert(index, '.')


# Example 1 should be 374
print(part1(parse("example1.txt")))
# Part 1 answer is 9805264
print(part1(parse("input.txt")))

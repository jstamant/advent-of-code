# day10.py

# Find the furthest point in the loop of pipes.
# This is a pathfinding problem. I'll use depth-first to solve it

import re

def parse(filename):
    file = open(filename, 'r')
    data = []
    for line in file:
        data.append(list(line)[:-1])
    file.close()
    return data

# I do a depth-first pathfinding to get the length of the loop.
# Then, the furthest distance is simply dividing the length by two
def part1(data):
    # Find starting point
    start = -1
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S': start = (x, y)
    print(f"Starting location is at {start}")

    path = []
    visited = {}

    try_point(start, path, data, visited)
    print('Length of the path is', len(path))
    return len(path) / 2

# Recursive function that returns the length of the connected pipe loop.
def try_point(point, path, graph, visited):
    print("Trying", point)
    # Base case: Point is out of bounds
    if point[0] < 0 or point[0] > len(graph[0])-1:
        return False
    if point[1] < 0 or point[1] > len(graph)-1:
        return False

    pipe_at_point = graph[point[1]][point[0]]
    previous_point = False
    previous_pipe = False
    if len(path) > 0:
        previous_point = path[-1]
        previous_pipe = graph[previous_point[1]][previous_point[0]]

    # Base cases for returning:
    # Pipe is invalid
    if pipe_at_point == '.':
        return False
    if point in visited:
        difference = len(path)-1 - visited[point]
        # if point was JUST visited (diff of 1)
        if difference == 1:
            return False
        # reached back to the start (larger than 1 AND pipe is an S)
        elif difference > 1 and pipe_at_point == 'S':
            return True
        # visited before (larger than 1)
        elif difference > 1 and pipe_at_point != 'S':
            return False

    # Pre-order actions
    visited[point] = visited[previous_point] + 1 if previous_point in visited else 0
    print("Pushing", point, pipe_at_point)
    path.append(point)

    # Recursing steps (but only check applicable directions)
    directions = []
    match pipe_at_point:
        # One problem: this is hard-coded to work on my own maze.
        # It might not look in the right direction on other mazes
        case 'S': directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        case '-': directions = [(-1, 0), (1, 0)]
        case '|': directions = [(0, -1), (0, 1)]
        case 'L': directions = [(0, -1), (1, 0)]
        case 'J': directions = [(0, -1), (-1, 0)]
        case 'F': directions = [(1, 0), (0, 1)]
        case '7': directions = [(-1, 0), (0, 1)]
    for dir in directions:
        if try_point((point[0]+dir[0], point[1]+dir[1]), path, graph, visited):
            return True

    # Post-order actions
    path.pop()
    return False

# Example 1 answer should be 4, example 2 should be 8
# print("example1.txt:")
# print(part1(parse("example1.txt")))
# print("example2.txt:")
# print(part1(parse("example2.txt")))

# Part 1 answer is 6725. The length of the loop is 13450
print("input.txt:")
print(part1(parse("input.txt")))

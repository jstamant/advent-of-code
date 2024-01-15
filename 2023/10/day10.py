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
    for line in data:
        print(line)

    # Find starting point
    start = -1
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S': start = (x, y)
    print(f"Starting location is at {start}")

    distance = 0
    stack = [start]
    visited = []
    for i in range(len(data)):
        visited.append([])
        for j in range(len(data[i])):
            visited[i].append('.')
    path = []

    return find_loop_length(stack, data, visited)

# Recursive function that returns the length of the connected pipe loop.
def find_loop_length(stack, graph, visited):
    point = stack[-1]
    pipe = graph[point[1]][point[0]]
    point_visit = visited[point[1]][point[0]]
    print(point, pipe)
    # if pipe == 'S' and :
    #     breakpoint()
    #     return
    if point_visit == 'X' or pipe == '.':
        print("Visited, or invalid pipe. Popping and returning.")
        stack.pop()
        return
    print(point_visit)

    visited[point[1]][point[0]] = 'X'

    if pipe == '-' or '7' or 'J' or 'S':
        if point[0] > 0:
            stack.append((point[0]-1, point[1]))
            find_loop_length(stack, graph, visited)
    if pipe == '-' or 'L' or 'F' or 'S':
        if point[0] < len(graph[0])-1:
            stack.append((point[0]+1, point[1]))
            find_loop_length(stack, graph, visited)
    if pipe == '|' or 'L' or 'J' or 'S':
        if point[1] > 0:
            stack.append((point[0], point[1]-1))
            find_loop_length(stack, graph, visited)
    if pipe == '|' or '7' or 'F' or 'S':
        if point[1] < len(graph)-1:
            stack.append((point[0], point[1]+1))
            find_loop_length(stack, graph, visited)

    print(stack)

    return len(stack)

# Example 1 answer should be 4, example 2 should be 8
print("example1.txt:")
print(part1(parse("example1.txt")))
# print("example2.txt:")
# print(part1(parse("example2.txt")))
# print("input.txt:")
# print(part1(parse("input.txt")))

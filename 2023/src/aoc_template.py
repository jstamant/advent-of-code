# aoc_template.py

def parse(filename):
    return

def part1(data):
    return

def part2(data):
    return

def solve(filename):
    data = parse(filename)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == '__main__':
    import sys
    for path in sys.argv[1:]:
        print(f"{path}:")

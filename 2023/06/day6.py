# day6.py

# Returns the time and distance of each race in the form
# [ [<time>, <dist>], [<time>, <dist>], ... ]
def parse(filename):
    file = open(filename, 'r')
    times = list(map(int, file.readline().split()[1:]))
    distances = list(map(int, file.readline().split()[1:]))
    file.close()
    data = []
    for i in range(len(times)): data.append([times[i], distances[i]])
    return data

# Returns the time and distance of each race in the form
# [ [<time>, <dist>], [<time>, <dist>], ... ]
# This is specifically for part 2
def parse2(filename):
    file = open(filename, 'r')
    times = file.readline().split()[1:]
    print(times.join())
    distances = file.readline().split()[1:]
    file.close()
    data = []
    for i in range(len(times)): data.append([times[i], distances[i]])
    return data

# Very rudimentary, but just iterate through all possible races
def get_number_of_winning_strategies(race_time, record_distance):
    sum = 0
    for time_pressed in range(1, race_time):
        velocity = time_pressed
        travel_distance = velocity * (race_time - time_pressed)
        if travel_distance > record_distance: sum += 1
    print(sum)
    return sum

def part1(data):
    product = 1
    for race in data:
        product *= get_number_of_winning_strategies(race[0], race[1])
    return product

# # example: answer is 288, which is 4 * 8 * 9
# data = parse("example.txt")
# print(part1(data))

# part 1: answer is 840336
data = parse2("input.txt")
print(data)
#print(part1(data))

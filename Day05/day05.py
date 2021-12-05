import numpy

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

expected = """.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111...."""

expected2 = """1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111...."""

def read_expected(expected):
    lines = expected.splitlines()
    grid = numpy.zeros((len(lines), len(lines[0])), dtype=int)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] != ".":
                grid[x, y] = int(lines[x][y])
    return grid

with open('input') as f:
    input = f.read().rstrip()

def parse_data(input):
    lines = input.splitlines()
    vents = []
    for line in lines:
        corners = line.split("->")
        origin = corners[0].split(",")
        destination = corners[1].split(",")
        if int(origin[0]) <= int(destination[0]):
            vents.append({"from": (int(origin[0]), int(origin[1])), "to": (int(destination[0]), int(destination[1]))})
        else:
            vents.append({"from": (int(destination[0]), int(destination[1])), "to": (int(origin[0]), int(origin[1]))})
    return vents

def trace(line, grid, straight_only=True):
    if line["to"][0] == line["from"][0]:
        if line["from"][1] <= line["to"][1]:
            grid[line["from"][0], line["from"][1]:line["to"][1]+1] += 1
        else:
            grid[line["from"][0], line["to"][1]:line["from"][1]+1] += 1
    elif line["to"][1] == line["from"][1]:
        grid[line["from"][0]:line["to"][0]+1, line["from"][1]] += 1
    else:
        if not straight_only:
            slope = float(line["to"][1] - line["from"][1]) / float(line["to"][0] - line["from"][0])
            for x in range(line["from"][0], line["to"][0] + 1):
                grid[x, int(round(line["from"][1] + slope * (x - line["from"][0])))] += 1
    return grid

def get_size(data):
    x = 0
    y = 0
    for line in data:
        if line["from"][0] > x:
            x = line["from"][0]
        if line["to"][0] > x:
            x = line["to"][0]
        if line["from"][1] > y:
            y = line["from"][1]
        if line["to"][1] > y:
            y = line["to"][1]
    return x + 1, y + 1

test_data = parse_data(test_input)
x, y = get_size(test_data)
test_grid = numpy.zeros((x,y), dtype=int)
for line in test_data:
    test_grid = trace(line, test_grid)

test_expected = read_expected(expected)
assert x == 10, "numbers of rows in grid should be 10"
assert y == 10, "numbers of cols in grid should be 10"
assert numpy.all(numpy.transpose(test_grid) == test_expected), "result grid should match expected"
assert numpy.count_nonzero(test_grid > 1) == 5, "Number of points with a value of at least 2"
print("Test part 1 result: %d points"%numpy.count_nonzero(test_grid > 1))
print()

data = parse_data(input)
x, y = get_size(data)
grid = numpy.zeros((x, y), dtype=int)
for line in data:
    grid = trace(line, grid)

print("Part 1 result: %d"%numpy.count_nonzero(grid > 1))
print()
print()

## Part2
x, y = get_size(test_data)
test_grid = numpy.zeros((x,y), dtype=int)
for line in test_data:
    test_grid = trace(line, test_grid, straight_only=False)

test_expected2 = read_expected(expected2)
assert x == 10, "numbers of rows in grid should be 10"
assert y == 10, "numbers of cols in grid should be 10"
assert numpy.all(numpy.transpose(test_grid) == test_expected2), "result grid should match expected"
assert numpy.count_nonzero(test_grid > 1) == 12, "Number of points with a value of at least 2"
print("Test part 2 result: %d points"%numpy.count_nonzero(test_grid > 1))
print()

x, y = get_size(data)
grid = numpy.zeros((x, y), dtype=int)
for line in data:
    grid = trace(line, grid, straight_only=False)

print("Part 2 result: %d"%numpy.count_nonzero(grid > 1))

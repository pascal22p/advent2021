import numpy

test_input = """3,4,3,1,2"""

test_expected = """3,4,3,1,2
2,3,2,0,1
1,2,1,6,0,8
0,1,0,5,6,7,8
6,0,6,4,5,6,7,8,8
5,6,5,3,4,5,6,7,7,8
4,5,4,2,3,4,5,6,6,7
3,4,3,1,2,3,4,5,5,6
2,3,2,0,1,2,3,4,4,5
1,2,1,6,0,1,2,3,3,4,8
0,1,0,5,6,0,1,2,2,3,7,8
6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8"""

with open('input') as f:
    input = f.read().rstrip()

def parse_data(input):
    days, counts = numpy.unique(numpy.array(input.split(",")).astype(int), return_counts=True)
    data = numpy.zeros((9), dtype=int)
    for day, count in zip(days, counts):
        data[day] = count
    return data

def new_generation(data):
    day_zero = data[0]
    data[0:-1] = data[1:]
    data[6] += day_zero
    data[8] = day_zero
    return data

data_expected = list(map(parse_data, test_expected.splitlines()))


## Part1
# Test
test_data = parse_data(test_input)
for day in range(0, 18):
    assert numpy.all(data_expected[day] == test_data)
    test_data = new_generation(test_data)

test_number_fish = numpy.sum(test_data)
print("%d fishes found after 26 days"%test_number_fish)
assert test_number_fish == 26, "number of fishes should be 26"

test_data = parse_data(test_input)
for day in range(0, 80):
    test_data = new_generation(test_data)

test_number_fish = numpy.sum(test_data)
print("Test 1 result: %d fishes found after 80 days"%test_number_fish)
assert test_number_fish == 5934, "number of fishes should be 5934"

data = parse_data(input)
for day in range(0, 80):
    data = new_generation(data)
number_fish = numpy.sum(data)
print("Part 1 result: %d fishes found after 80 days"%number_fish)

print()
print()

## part 2
# test
test_data = parse_data(test_input)
for day in range(0, 256):
    test_data = new_generation(test_data)

test_number_fish = numpy.sum(test_data)
print("Test 2 result: %d fishes found after 80 days"%test_number_fish)
assert test_number_fish == 26984457539, "number of fishes should be 26984457539"

data = parse_data(input)
for day in range(0, 256):
    data = new_generation(data)
number_fish = numpy.sum(data)
print("Part 2 result: %d fishes found after 80 days"%number_fish)

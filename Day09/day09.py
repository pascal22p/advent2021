import numpy
import sys

test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

with open('input') as f:
    input = f.read().rstrip()

def parse_input(input):
    data = []
    for line in input.strip().splitlines():
        data.append(list(line))
    return numpy.array(data, dtype=int)

def find_local_minima(data):
    shape = numpy.shape(data)
    work_array = numpy.full(tuple(x + 2 for x in shape), numpy.max(data) + 1)
    work_array[1:-1,1:-1] = data
    results = []
    locations = []

    for i in range(1, shape[0] + 1):
        for j in range(1, shape[1] + 1):
            if numpy.all(work_array[i,j] <= work_array[i-1:i+2,j-1:j+2]):
                results.append(work_array[i,j])
                locations.append((i-1,j-1))
    return locations, numpy.array(results)

def paint_basin(data, location):
    work_array = numpy.copy(data)
    shape = numpy.shape(data)

    row = location[0]
    col = location[1]

    def count(i, j):
        result = 1
        work_array[i,j] = 9

        if i - 1 >= 0 and work_array[i-1,j] == -1:
            work_array[i-1,j] = 9
            result += count(i-1,j)
        if j - 1 >= 0 and work_array[i,j-1] == -1:
            work_array[i,j-1] = 9
            result += count(i,j-1)
        if j + 1 < shape[1] and work_array[i,j+1] == -1:
            work_array[i,j+1] = 9
            result += count(i,j+1)
        if i + 1 < shape[0] and work_array[i+1,j] == -1:
            work_array[i+1,j] = 9
            result += count(i+1,j)
        return result

    return count(row, col)

def part2(data, locations):
    basins_count = []
    mask = numpy.where(data == numpy.max(data),0,-1)
    for location in locations:
        basins_count.append(paint_basin(mask, location))
    return basins_count

test_data = parse_input(test_input)
test_shape = numpy.shape(test_data)
test_locations, test_minima = find_local_minima(test_data)
test_part1_result = numpy.sum(test_minima + 1)
print("Test part 1 result: %d"%test_part1_result)
assert test_part1_result == 15, "sum of lowest risking should be 15"

data = parse_input(input)
locations, minima = find_local_minima(data)
part1_result = numpy.sum(minima + 1)
print("Part 1 result: %d"%part1_result)
print()
print()

expected_basins = [3,9,9,14]
basins_count = part2(test_data, test_locations)
print("Basins counts are: " + str(basins_count))
assert sorted(basins_count) == expected_basins, "basins sizes should be " + str(expected_basins)
test_part2_result = numpy.prod(sorted(basins_count)[-3:])
assert test_part2_result == 1134, "Test part 2 result should be 1134"
print("Test part2 result: %d"%test_part2_result)

basins_count = part2(data, locations)
part2_result = numpy.prod(sorted(basins_count)[-3:])
print("Part2 result: %d"%part2_result)

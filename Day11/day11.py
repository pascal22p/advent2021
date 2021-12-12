import numpy
import sys

def parse_input(input):
    data = []
    for line in input.strip().splitlines():
        data.append(list(line))
    return numpy.array(data, dtype=int)

test_input = """11111
19991
19191
19991
11111"""

test_input_large= """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

expected = []
expected.append(parse_input("""34543
40004
50005
40004
34543"""))

expected.append(parse_input("""45654
51115
61116
51115
45654"""))

expected_large = []
expected_large.append(parse_input("""6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""))

expected_large.append(parse_input("""8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""))

expected_large.append(parse_input("""0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000"""))

expected_large.append(parse_input("""2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211"""))

expected_large100 = parse_input("""0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766""")



with open('input') as f:
    input = f.read().rstrip()

def next_generation(data):

    def flash_neighbours(data, coordinates):
        shape = numpy.shape(data)
        flashes_count_inner = 0
        for coordinate in coordinates:
            data[max(0, coordinate[0]-1):min(shape[0], coordinate[0]+2), max(0, coordinate[1]-1):min(shape[1], coordinate[1]+2)] += 1
            flashes = numpy.nonzero(data[max(0, coordinate[0]-1):min(shape[0], coordinate[0]+2), max(0, coordinate[1]-1):min(shape[1], coordinate[1]+2)] == 10)
            if len(flashes[0]) > 0:
                flashes_count_inner += len(flashes[0])
                newcoordinates = [(i, j) for i, j in zip(flashes[0]+max(0, coordinate[0]-1), flashes[1]+max(0, coordinate[1]-1))]
                flashes_count_inner += flash_neighbours(data, newcoordinates)
        return flashes_count_inner

    data += 1
    flashes = numpy.nonzero(data == 10)
    flashes_count = len(flashes[0])
    coordinates = [(i, j) for i, j in zip(flashes[0], flashes[1])]
    flashes_count_inner = flash_neighbours(data, coordinates)
    return numpy.where(data > 9, 0, data), flashes_count + flashes_count_inner


## Tests
test_data = parse_input(test_input)

for i in range(2):
    test_data, flashes = next_generation(test_data)
    assert numpy.all(expected[i] == test_data)

test_data_large = parse_input(test_input_large)
for i in range(4):
    test_data_large, flashes = next_generation(test_data_large)
    assert numpy.all(expected_large[i] == test_data_large)

test_data_large = parse_input(test_input_large)
total_flashes = 0
for i in range(100):
    test_data_large, flashes = next_generation(test_data_large)
    total_flashes += flashes
assert numpy.all(expected_large100 == test_data_large)
print("Test part1 result: %d"%total_flashes)
assert total_flashes == 1656, "Number of flashes should be 1656"

## Part 1
data = parse_input(input)
total_flashes = 0
for i in range(100):
    data, flashes = next_generation(data)
    total_flashes += flashes
print("Part1 result: %d"%total_flashes)
print()
print()

## Part 2
data = parse_input(input)
step = 0
while not numpy.all(data == 0):
    step += 1
    data, flashes = next_generation(data)
print("Part2 result: %d"%step)

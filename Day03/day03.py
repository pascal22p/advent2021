import numpy

#numpy.genfromtxt('arr.txt', dtype=bool)

test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

with open('input') as f:
    input = f.read().rstrip()

def parse_data(input):
    return numpy.array([[int(char) for char in list(line)] for line in input.splitlines()])

def bits_to_int(bits):
    return int("".join(str(i) for i in bits),2)

def gamma_rate(diagnostic_report):
    return bits_to_int((numpy.count_nonzero(diagnostic_report, 0) > numpy.shape(diagnostic_report)[0] / 2).astype(int))

def epsilon_rate(diagnostic_report):
    return bits_to_int((numpy.count_nonzero(diagnostic_report, 0) < numpy.shape(diagnostic_report)[0] / 2).astype(int))

def measure_rating(diagnostic_report, index = 0, direction = -1):
    def get_digit(a, direction):
        if direction == -1:
            return 0 if (numpy.sum(a) >= len(a) / 2.0) else 1
        else:
            return 1 if (numpy.sum(a) >= len(a) / 2.0) else 0

    def recursive(diagnostic_report, index):
        if numpy.shape(diagnostic_report)[0] == 1:
            result = [diagnostic_report[0, index:]]
        else:
            digit = get_digit(diagnostic_report[:,index], direction)
            indices = numpy.argwhere(diagnostic_report[:,index] == digit).flatten()
            if index < numpy.shape(diagnostic_report)[1] - 1:
                result = numpy.insert(recursive(diagnostic_report[indices, :], index + 1), 0, digit).astype(int)
            else:
                result = [digit]
        return result

    result = recursive(diagnostic_report, index)
    return bits_to_int(result)

## Part 1
# Test
test_data = parse_data(test_input)

assert bits_to_int([1,0,1,0,1,0]) == 42
assert gamma_rate(test_data) == 22, "Gamma rate should be 22"
assert epsilon_rate(test_data) == 9, "Epsilon rate should be 9"

print("Test Gamma rate is %d"%gamma_rate(test_data))
print("Test Epsilon rate is %d"%epsilon_rate(test_data))
print("Test Part 1 result is %d"%(gamma_rate(test_data) * epsilon_rate(test_data)))
print()

data = parse_data(input)
print("Gamma rate is %d"%gamma_rate(data))
print("Epsilon rate is %d"%epsilon_rate(data))
print("Part 1 result is %d"%(gamma_rate(data) * epsilon_rate(data)))
print()
print()

## Part 2
# test
oxygen = measure_rating(test_data, direction = 1)
assert oxygen == 23
print("Test part 2: oxygen rate is %d"%oxygen)
co2 = measure_rating(test_data, direction = -1)
assert co2 == 10
print("Test part 2: co2 rate is %d"%co2)
print()

oxygen = measure_rating(data, direction = 1)
print("Part 2: oxygen rate is %d"%oxygen)
co2 = measure_rating(data, direction = -1)
print("Part 2: co2 rate is %d"%co2)
print("Part 2 result is %d"%(oxygen * co2))

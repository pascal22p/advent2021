import numpy
import math

test_data = numpy.array([16,1,2,0,4,2,7,1,2,14], dtype=int)

def calculate_fuel(data, target):
    return numpy.sum(numpy.abs(data - target))

def calculate_fuel2(data, target):
    return numpy.sum(numpy.abs(data - target)*(1 + numpy.abs(data - target)) / 2).astype(int)

def solve_minimum(data):
    # distance of a point xi to a target T is (xi - T)(1 + xi - T)/2
    # We want to minimise SUM(abs((xi - T)(1 + xi - T)/2)) over all i points
    # This is the same as minimising (xi - T)^2 * (1 + xi -T)^2
    # At the minimum the first derivative is zero: SUM( 2 (-T + xi) (1 - T + xi) (1 - 2 T + 2 xi) ) = 0
    # The second derivative is negative but it will be quicker to just check each integer solution of the roots above.

    root1 = numpy.sum(data)/numpy.size(data) # SUM( (-T + xi) ) = 0 Note
    root2 = (numpy.sum(data) + numpy.size(data))/numpy.size(data) # SUM( (1 - T + xi) ) = 0
    root3 = (numpy.sum(2.0 * data) + numpy.size(data)) / (numpy.size(data) * 2.0) # SUM( (1 - 2 T + 2 xi) ) = 0

    targets = numpy.unique(numpy.array([int(root1), int(root2), int(root3), int(math.ceil(root1)), int(math.ceil(root2)), int(math.ceil(root3))]))

    minimums = numpy.array([[target, calculate_fuel2(data, target)] for target in targets])
    return minimums[numpy.argmin(minimums[:,1])]

## Part 1

test_fuel = calculate_fuel(test_data, int(numpy.median(test_data)))
assert test_fuel == 37, "necessary fuel should be 37"
print("Test part 1 result: %d"%test_fuel)


data = numpy.loadtxt("input", delimiter=",", dtype=int)
fuel = calculate_fuel(data, int(numpy.median(data)))
print("Part 1 result: %d"%fuel)
print()
print()

## Part 2

test_result = solve_minimum(test_data)
assert test_result[0] == 5, "Target should be 5"
assert test_result[1] == 168, "fuel cost should 168"
print("Test part 2 result: %d"%test_result[1])

result = solve_minimum(data)
print("Test part 2 result: %d"%result[1])

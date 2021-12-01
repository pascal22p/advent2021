import numpy

def count_increase(input):
    return numpy.count_nonzero((input[1:] - input[0:-1]) > 0)

def sliding_window(input):
    return numpy.convolve(input,numpy.ones(3,dtype=int),'valid')

test_input = numpy.array([199, 200 ,208, 210, 200, 207, 240, 269, 260, 263])
input = numpy.loadtxt("input")

## Part 1
# test
print("Test part 1 result: %d"%count_increase(test_input))

print("Part 1 Result: %d"%count_increase(input))


print("Test part 2 result: %d"%count_increase(sliding_window(test_input)))

print("Part 2 Result: %d"%count_increase(sliding_window(input)))

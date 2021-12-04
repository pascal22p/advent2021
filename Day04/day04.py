import numpy
import io
import sys

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

with open('input') as f:
    input = f.read().rstrip()

def parse_data(input):
    lines = input.split("\n\n")
    draws = numpy.array(lines[0].split(",")).astype(int)

    boards = []
    for block in lines[1:]:
        f_handler = io.StringIO(block)
        boards.append(numpy.loadtxt(f_handler, dtype=int))
        f_handler.close()

    return draws, numpy.array(boards)


def play_bingo(draws, boards):
    for draw in draws:
        boards = numpy.where(boards == draw, 0, boards)
        result = numpy.concatenate((numpy.sum(boards, (2)), numpy.sum(boards, (1))), axis=1)
        winners = numpy.any(result == 0, axis=1)
        if (numpy.count_nonzero(winners) == 1):
            index = numpy.where(winners)[0]
            break

    return draw, boards[index]

def loose_bingo(draws, boards):
    for draw in draws:
        boards = numpy.where(boards == draw, 0, boards)
        result = numpy.concatenate((numpy.sum(boards, (2)), numpy.sum(boards, (1))), axis=1)
        winners = numpy.any(result == 0, axis=1)
        if (len(winners) - numpy.count_nonzero(winners) == 1):
            index = numpy.where(winners == False)[0]
            break

    return index

## Part 1
# Test
test_draws, test_boards = parse_data(test_input)
draw, board = play_bingo(test_draws, test_boards)

assert draw == 24, "last draw should be 24"
assert numpy.sum(board) == 188, "Maximum score should be 188"

print("Test Part 1 result is %d"%(draw * numpy.sum(board)))
print()

draws, boards = parse_data(input)
draw, board = play_bingo(draws, boards)
print("Part 1 result is %d"%(draw * numpy.sum(board)))
print()
print()

## Part 1
# Test
loosing = loose_bingo(test_draws, test_boards)
draw, board = play_bingo(test_draws, test_boards[loosing])

assert draw == 13, "last draw should be 13"
assert numpy.sum(board) == 148, "Maximum score should be 148"

print("Test Part 2 result is %d"%(draw * numpy.sum(board)))
print()

loosing = loose_bingo(draws, boards)
draw, board = play_bingo(draws, boards[loosing])
print("Part 2 result is %d"%(draw * numpy.sum(board)))

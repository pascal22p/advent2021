import numpy
import itertools

test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

test_input2 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

expected = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]

with open('input') as f:
    input = f.read().rstrip()

def parse_input(input):
    data = []
    for line in input.strip().splitlines():
        signal = line.split("|")
        data.append({"pattern":signal[0].strip().split(" "), "output":signal[1].strip().split(" ")})
    return data

def count_part1(data):
    score = numpy.zeros((10), dtype=int)
    for signal in data:
        for output in signal["output"]:
            score[len(output)] += 1
    return score

def code_to_number(code, segments):
    # --  0
    #|  | 1, 2
    # __  3
    #|  | 4, 5
    # __  6

    zero = {0,2,5,6,4,1}
    one = {2,5}
    two = {0,2,3,4,6}
    three = {0,2,5,6,3}
    four = {1,2,3,5}
    five = {0,1,3,5,6}
    six = {0,1,4,6,5,3}
    seven = {0,2,5}
    eight = {0,1,2,3,4,5,6}
    nine = {0,2,5,6,3,1}

    numeric_code = set()
    for letter in code:
        numeric_code.add(segments.index(letter))

    if numeric_code == zero:
        result = 0
    elif numeric_code == one:
        result = 1
    elif numeric_code == two:
        result = 2
    elif numeric_code == three:
        result = 3
    elif numeric_code == four:
        result = 4
    elif numeric_code == five:
        result = 5
    elif numeric_code == six:
        result = 6
    elif numeric_code == seven:
        result = 7
    elif numeric_code == eight:
        result = 8
    elif numeric_code == nine:
        result = 9
    else:
        result = None

    return result


def solve_part2(data):
    results = []
    for signal in data:
        numbers = {}
        for subset in itertools.permutations("abcdefg"):
            # --  0
            #|  | 1, 2
            # __  3
            #|  | 4, 5
            # __  6

            numbers[0] = subset[0]+subset[1]+subset[2]+subset[4]+subset[5]+subset[6]
            numbers[1] = subset[2]+subset[5]
            numbers[2] = subset[0]+subset[2]+subset[3]+subset[4]+subset[6]
            numbers[3] = subset[0]+subset[2]+subset[3]+subset[5]+subset[6]
            numbers[4] = subset[1]+subset[2]+subset[3]+subset[5]
            numbers[5] = subset[0]+subset[1]+subset[3]+subset[5]+subset[6]
            numbers[6] = subset[0]+subset[1]+subset[3]+subset[4]+subset[5]+subset[6]
            numbers[7] = subset[0]+subset[2]+subset[5]
            numbers[8] = subset[0]+subset[1]+subset[2]+subset[3]+subset[4]+subset[5]+subset[6]
            numbers[9] = subset[0]+subset[1]+subset[2]+subset[3]+subset[5]+subset[6]

            ok = True
            for output in signal["pattern"]:
                if len(output) == 2: # Number 1
                    if "".join(sorted(output))!="".join(sorted(numbers[1])):
                        ok = False
                        break
                if len(output) == 4: # number 4
                    if "".join(sorted(output))!="".join(sorted(numbers[4])):
                        ok = False
                        break
                if len(output) == 3: # Number 7
                    if "".join(sorted(output))!="".join(sorted(numbers[7])):
                        ok = False
                        break

            if ok:
                result = ""
                for number in signal["output"]:
                    num = code_to_number(number, subset)
                    if num is None:
                        ok = False
                        break
                    result += str(num)
                if ok:
                    results.append(int(result))
                    break
    return results

unique_digits_len = [2,4,3,7]

test_data = parse_input(test_input)
test_part1_result = numpy.sum(count_part1(test_data)[unique_digits_len])
print("Test part 1 result: %d"%test_part1_result)
assert test_part1_result == 26, "number of occurences should be 26"

data = parse_input(input)
part1_result = numpy.sum(count_part1(data)[unique_digits_len])
print("Part 1 result: %d"%part1_result)
print()
print()

test_data2 = parse_input(test_input2)
test_part2_result2 = solve_part2(test_data2)[0]
print("Test part 2.2 result: %d"%test_part2_result2)
assert test_part2_result2 == 5353, "output should be 5353"

test_part2_result1 = solve_part2(test_data)
print("Test part 2.1 result: %d"%numpy.sum(test_part2_result1))
assert numpy.sum(test_part2_result1) == 61229, "output should be 61229"
assert numpy.all(test_part2_result1 == expected), "outputs should match" + str(expected)

part2_result = solve_part2(data)
print("Part 2 result: %d"%numpy.sum(part2_result))

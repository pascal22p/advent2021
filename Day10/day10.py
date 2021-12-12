
test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

with open('input') as f:
    input = f.read().rstrip()

def check_bracket(acc, closing_bracket):
    if len(acc) >0:
        if acc[-1] == closing_bracket:
            return True
    return False


test_data = test_input.strip().splitlines()
data = input.strip().splitlines()

brackets = {")":"(", "}":"{", "]":"[", ">":"<"}

def validate_string(s):
    acc = []
    error = 0
    for index, char in enumerate(s):
        if char in brackets.values():
            acc.append(char)
        elif char in brackets.keys():
            check = check_bracket(acc, brackets[char])
            if check:
                acc.pop()
            else:
                error = (index, char)
                break
        else:
            raise ValueError("Should not be here")

    return "".join(acc), error

def part1(data):
    score_table = {")":3, "]":57, "}":1197, ">":25137}
    score = 0
    for line in data:
        result, error = validate_string(list(line))
        if error != 0:
            score += score_table[error[1]]
    return score

def part2(data):
    def score(s):
        score_table = {")":1, "]":2, "}":3, ">":4}
        score = 0
        for char in s:
            score = score * 5 + score_table[char]
        return score

    reverse = {val:key for key, val in brackets.items()}
    scores = {}
    for line in data:
        result, error = validate_string(list(line))
        if error == 0:
            complete = [reverse[char] for char in list(result)[::-1]]
            scores["".join(complete)] = score(complete)
    return scores

test_part1_result = part1(test_data)
print("Test part1 result: %d"%test_part1_result)
assert test_part1_result == 26397, "score should be 26397"

part1_result = part1(data)
print("Part1 result: %d"%part1_result)
print()
print()


expected = {"}}]])})]": 288957, ")}>]})": 5566, "}}>}>))))":1480781, "]]}}]}]}>": 995444, "])}>": 294}

test_part2_result = part2(test_data)
for result, score in test_part2_result.items():
    if result in expected:
        assert expected[result] == score, "Score should be %d"%expected[result]
    else:
        print(result, score)
        raise ValueError("Test part 2 not passing")

scores = sorted(list(test_part2_result.values()))
print("Test part2 result: %d"%scores[len(scores)//2])
assert scores[len(scores)//2] == 288957, "score should be 288957"

part2_result = part2(data)
scores = sorted(list(part2_result.values()))
print("Part2 result: %d"%scores[len(scores)//2])

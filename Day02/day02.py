from itertools import groupby


test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

with open('input') as f:
    input = f.read().rstrip()

def parse_input(input):
    commands = []
    for line in input.splitlines():
        command = line.split(" ")
        commands.append({command[0]: int(command[1])})
    return commands

def group_by(commands):
    grouped_commands = {}
    for command in commands:
        key = list(command.keys())[0]
        value = command[key]
        if key in grouped_commands:
            grouped_commands[key] = grouped_commands[key] + value
        else:
            grouped_commands[key] = value
    return grouped_commands

def aggregate(commands):
    return (commands["down"] - commands["up"]) * commands["forward"]

# Test Part 1
grouped_commands = group_by(parse_input(test_input))
print("Grouped commands test part 1: %s"%str(grouped_commands))
print("Result test part 1: %d"%aggregate(grouped_commands))

# Part 1
grouped_commands = group_by(parse_input(input))
print("Grouped commands test part 1: %s"%str(grouped_commands))
print("Result test part 1: %d"%aggregate(grouped_commands))

print("########")

def group_by_part2(commands):
    grouped_commands = {"aim":0, "forward":0, "depth":0}
    for command in commands:
        key = list(command.keys())[0]
        value = command[key]
        if key == "up":
            grouped_commands["aim"] = grouped_commands["aim"] - value
        elif key == "down":
            grouped_commands["aim"] = grouped_commands["aim"] + value
        elif key == "forward":
            grouped_commands["forward"] = grouped_commands["forward"] + value
            grouped_commands["depth"] = grouped_commands["depth"] + value * grouped_commands["aim"]
    return grouped_commands

def aggregate_part2(commands):
    return commands["depth"] * commands["forward"]


# Test Part 2
grouped_commands = group_by_part2(parse_input(test_input))
print("Grouped commands test part 2: %s"%str(grouped_commands))
print("Result test part 2: %d"%aggregate_part2(grouped_commands))
grouped_commands = group_by_part2(parse_input(input))
print("Grouped commands test part 2: %s"%str(grouped_commands))
print("Result test part 2: %d"%aggregate_part2(grouped_commands))

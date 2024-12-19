# Advent of Code 2024 - Day 7 solution

from itertools import product


def parse_equation(line: str) -> tuple[int, list[int]]:
    parts = line.split(": ")
    return int(parts[0]), [int(i) for i in parts[1].split(" ")]

def could_be_true(equation):
    test_value, values = equation

    operations = {
        "+": lambda x, y: x+y,
        "*": lambda x, y: x*y
    }
    
    for combo in product(operations.keys(), repeat=len(values)-1):
        result = values[0]
        for op, v in zip(combo, values[1:]):
            result = operations[op](result, v)
        if result == test_value:
            return True
    return False


def could_be_true_part2(equation):
    test_value, values = equation

    operations = {
        "+": lambda x, y: x+y,
        "*": lambda x, y: x*y,
        "||": lambda x, y: (int(str(x) + str(y)))
    }
    
    for combo in product(operations.keys(), repeat=len(values)-1):
        result = values[0]
        for op, v in zip(combo, values[1:]):
            result = operations[op](result, v)
        if result == test_value:
            return True
    return False





def part1():
    with open("day07/input.txt") as f:
        lines = f.readlines()
    equations = [parse_equation(line) for line in lines]

    total = sum([e[0] for e in equations if could_be_true(e)])
    print("Part 1:", total)


def part2():
    with open("day07/input.txt") as f:
        lines = f.readlines()
    equations = [parse_equation(line) for line in lines]

    total = sum([e[0] for e in equations if could_be_true_part2(e)])
    print("Part 1:", total)

if __name__ == "__main__":
    part1()
    part2()      

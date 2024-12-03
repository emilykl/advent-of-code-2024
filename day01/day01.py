# Advent of Code 2024 - Day 1 solution

from collections import Counter


def part1():
    with open("day01/input.txt") as f:
        lines = f.readlines()
    splits = [line.strip().split() for line in lines]
    numbers = [(int(s[0]), int(s[1])) for s in splits if len(s) == 2]
    x, y = zip(*numbers)
    x = sorted(x)
    y = sorted(y)

    result = 0
    for i, j in zip(x, y):
        result += abs(i - j)

    print("Part 1:", result)
    
def part2():
    with open("day01/input.txt") as f:
        lines = f.readlines()
    splits = [line.strip().split() for line in lines]
    numbers = [(int(s[0]), int(s[1])) for s in splits if len(s) == 2]
    x, y = zip(*numbers)

    count_x = Counter(x)
    count_y = Counter(y)

    result = 0
    for num, count in count_x.items():
        result += num * count * count_y.get(num, 0)

    print("Part 2:", result)


if __name__ == "__main__":
    part1()
    part2()      

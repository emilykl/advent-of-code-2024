# Advent of Code 2024 - Day 3 solution

import re


def product(match):
    match = match[4:-1]
    parts = match.split(",")
    return int(parts[0]) * int(parts[1])

def part1():
    with open("day03/input.txt") as f:
        text = f.read().strip()
    
    # Find all mul(X,Y) instructions using regex
    matches = re.findall(r"mul\(\d+,\d+\)", text)
    
    # Parse each mul() command and compute the product 
    products = [product(m) for m in matches]
    result = sum(products)
    print("Part 1:", result)


def part2():
    with open("day03/input.txt") as f:
        text = f.read().strip()

    matches = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", text)
    
    enabled = True
    result = 0
    for m in matches:
        if m[0]:  # mul(X,Y)
            if enabled:
                result += product(m[0])
        elif m[1]:  # do()
            enabled = True
        else:  # don't()
            enabled = False


    print("Part 2:", result)


if __name__ == "__main__":
    part1()
    part2()      

# Advent of Code 2024 - Day 4 solution

import numpy as np


def make_diag1(lines_horiz):
    # Start in the bottom right corner
    lines_diag1 = []
    for r in range(len(lines_horiz)-1, -len(lines_horiz)-1, -1):
        curr_line = []
        i = r
        j = 0
        while i < len(lines_horiz) and j < len(lines_horiz[i]):
            if i >= 0:
                curr_line.append(lines_horiz[i][j])
            i += 1
            j += 1
        lines_diag1.append(curr_line)
    return lines_diag1

def make_diag2(lines_horiz):
    # Start in the bottom left corner
    lines_diag1 = []
    for r in range(len(lines_horiz)-1, -len(lines_horiz)-1, -1):
        curr_line = []
        i = r
        j = len(lines_horiz[i])-1
        while i < len(lines_horiz) and j >= 0:
            if i >= 0:
                curr_line.append(lines_horiz[i][j])
            i += 1
            j -= 1
        lines_diag1.append(curr_line)
    return lines_diag1

def count_xmas(lines):
    total = 0
    for line in lines:
        total += line.count("XMAS")
        total += line.count("SAMX")
    return total

def part1():
    with open("day04/input.txt") as f:
        lines = f.readlines()
    lines_horiz = [[c for c in line.strip()] for line in lines]
    lines_vert = list(zip(*lines_horiz))

    # Horizontal and vertical are straightforward, but we need to
    # make the diagonal lines too
    # I have hidden all the ugly logic inside functions
    lines_diag1 = make_diag1(lines_horiz)
    lines_diag2 = make_diag2(lines_horiz)

    # Now that we have the horizontal and vertical and diagonal lines,
    # join them back up into strings
    lines_horiz = ["".join(line) for line in lines_horiz]
    lines_vert = ["".join(line) for line in lines_vert]
    lines_diag1 = ["".join(line) for line in lines_diag1]
    lines_diag2 = ["".join(line) for line in lines_diag2]

    # Count the appearances of `XMAS` or `SAMX` (XMAS backwards)
    result = 0
    result += count_xmas(lines_horiz)
    result += count_xmas(lines_vert)
    result += count_xmas(lines_diag1)
    result += count_xmas(lines_diag2)

    print("Part 1:", result)


def is_x_mas(sub_array):
    x_mas = np.array([
        ["M",".","M"],
        [".","A","."],
        ["S",".","S"],
    ])

    return sub_array[0,0] == x_mas[0,0] \
        and sub_array[0,2] == x_mas[0,2] \
        and sub_array[1,1] == x_mas[1,1] \
        and sub_array[2,0] == x_mas[2,0] \
        and sub_array[2,2] == x_mas[2,2]

def part2():
    # Load input file into a numpy array
    with open("day04/input.txt") as f:
        lines = f.readlines()
    lines_horiz = [[c for c in line.strip()] for line in lines]

    input_array = np.array(lines_horiz)
  
    # Iterate through every 3x3 square in the input array
    x_mas_count = 0
    for i in range(input_array.shape[0]-2):
        for j in range(input_array.shape[1]-2):
            sub_array = input_array[i:i+3,j:j+3]

            # Check if any orientation of the sub array is x-mas
            match = \
                is_x_mas(sub_array) \
                or is_x_mas(np.rot90(sub_array, k=1)) \
                or is_x_mas(np.rot90(sub_array, k=2)) \
                or is_x_mas(np.rot90(sub_array, k=3))
            
            if match:
                x_mas_count += 1
                if not sub_array[0,0] == sub_array[0,2]:
                    print(sub_array)

    print("Part 2:", x_mas_count)


if __name__ == "__main__":
    part1()
    part2()      

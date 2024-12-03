# Advent of Code 2024 - Day 2 solution

def load_reports():
    with open("day02/input.txt") as f:
        reports = f.readlines()
    reports = [report.split() for report in reports]
    reports = [[int(level) for level in report] for report in reports]
    return reports

def is_safe_dampened(report, threshold=3):
    if is_safe(report, threshold=threshold):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report, threshold=threshold):
            return True
    return False


def is_safe(report, threshold=3):
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    return all([d>0 and d<=threshold for d in diffs]) or all([d<0 and d>=-threshold for d in diffs])


def part1():
    reports = load_reports()

    result = 0
    for report in reports:
        if is_safe(report):
            result += 1
    print("Part 1:", result)


def part2():
    reports = load_reports()

    result = 0
    for report in reports:
        if is_safe_dampened(report):
            result += 1
    print("Part 2:", result)


if __name__ == "__main__":
    part1()
    part2()      

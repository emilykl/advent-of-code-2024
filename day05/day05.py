# Advent of Code 2024 - Day 5 solution

from collections import Counter
import math


def get_rules_and_updates(input_filename):
    with open(input_filename) as f:
        lines = f.readlines()
    rule_lines = [line for line in lines if "|" in line]
    update_lines = [line for line in lines if "," in line]

    rules = [extract_rule(line) for line in rule_lines]
    updates = [extract_update(line) for line in update_lines]

    return rules, updates


def extract_rule(line):
    parts = line.strip().split("|")
    return [int(p) for p in parts]

def extract_update(line):
    parts = line.strip().split(",")
    return [int(p) for p in parts]

def middle(input_list):
    if len(input_list) % 2 == 0:
        raise ValueError("Input list must have an odd number of items")
    middle_index = math.floor(len(input_list) / 2)
    return input_list[middle_index]

def follows_rules(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

def part1():

    rules, updates = get_rules_and_updates("day05/input.txt")

    result = sum(
        [
            middle(update) 
            for update in updates 
            if follows_rules(update, rules)
        ]
    )

    print("Part 1:", result)


def sort_update(update, rules):
    local_sort_order = Counter(
        [
            r[1] 
            for r in rules
            if r[0] in update and r[1] in update
        ]
    )
    update_sorted = sorted(update, key=lambda x: local_sort_order.get(x,0))
    return update_sorted

def part2():
    rules, updates = get_rules_and_updates("day05/input.txt")

    incorrect_updates = [u for u in updates if not follows_rules(u, rules)]
    incorrect_updates_sorted = [sort_update(u, rules) for u in incorrect_updates]
    
    result = sum([middle(u) for u in incorrect_updates_sorted])

    print("Part 2:", result)


if __name__ == "__main__":
    part1()
    part2()      

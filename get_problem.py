import datetime
import os
import sys

from bs4 import BeautifulSoup
import requests


def main():
    # If day is passed as command-line argument, get problem for that day,
    # otherwise get problem for current day
    if len(sys.argv) > 1:
        day = sys.argv[1]
    else:
        # Get the current day
        day = datetime.datetime.now().day

    # Create directory for day
    create_dir(day)

    # Get problem and save to file `dayDD/problem.txt`
    get_problem(day)

    # Create boilerplate file `dayDD/dayDD.py` for solution
    make_solution_file(day)

    # Ideally, I want to also get the input file and save to `dayDD/input.txt`.
    # Haven't figured out how to do that yet though.
    # For now, just make an empty file.
    make_input_file(day)


# Create directory for the given day
def create_dir(day):
    dirpath = f"day{day:0>2}"
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    else:
        print(f"Directory `{dirpath}` already exists -- not overwriting!")


# Get problem and save to file `dayDD/problem.txt`
def get_problem(day):
    # Parse the HTML
    problem_url = f"https://adventofcode.com/2024/day/{day}"
    input_url = problem_url + "/input"

    print("\nProblem can be found at: ", problem_url)
    print("Input file can be found at: ", input_url, "\n")

    response = requests.get(problem_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Get all elements with the class `day-desc`
    # This will get the problem for Part One, and also for Part Two
    # if already revealed
    elements = soup.find_all(class_="day-desc")

    # Get the text inside the elements
    problem_text = "\n".join([element.text for element in elements])

    # Fix up the formatting a little
    problem_text = problem_text.replace(" ---", " ---\n")
    problem_text = problem_text.replace("\n", "\n\n")
    problem_text = problem_text.replace("\n\n\n\n", "\n\n")

    if not problem_text:
        print(f"\nProblem for day {day} has not been posted yet!\n")
        sys.exit(1)

    # Write to file
    # Note: This will overwrite the existing problem file ONLY if
    # the new text is longer than the existing text
    file_path = f"day{day:0>2}/problem.txt"

    if os.path.exists(file_path):
        with open(file_path) as f:
            if len(problem_text) >= len(f.read()):
                overwrite = True
            else:
                overwrite = False
    else:
        overwrite = True

    if overwrite:
        with open(file_path, "w") as f:
            f.write(problem_text)
        print(f"Day {day} problem statement written to {file_path}.")
    else:
        print(
            f"File {file_path} already exists with longer text content. Not overwriting."
        )

# Make an empty solution file at `dayDD.py`
def make_solution_file(day):
    file_path = f"day{day:0>2}/day{day:0>2}.py"

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(
                f"""# Advent of Code 2024 - Day {day} solution


def part1():
    with open("day{day:0>2}/input.txt") as f:
        pass
    result = None
    print("Part 1:", result)


def part2():
    result = None
    print("Part 2:", result)


if __name__ == "__main__":
    part1()
    part2()      
"""
            )
        print(f"Created empty solution file at {file_path}.")
    else:
        print(f"Solution file already exists at {file_path}. Not overwriting.")


# Make an empty input file at `input/dayDD.txt`
def make_input_file(day):
    file_path = input_file_path(day)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")
        print(f"Created empty input file at {file_path}.")
    else:
        print(f"Input file already exists at {file_path}. Not overwriting.")


def input_file_path(day):
    return f"day{day:0>2}/input.txt"


if __name__ == "__main__":
    main()

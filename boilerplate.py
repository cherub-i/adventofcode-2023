import sys
import os
import re

sys.path.insert(0, os.path.abspath("."))
day = "01"

def part_one(test_only):
    print("=== Part One ===")
    if test_only:
        the_file = "test_1.txt"
    else:
        the_file = "input.txt"
    print(f"file '{the_file}'")

    # timer = Timer()

    pattern = re.compile(
        r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )

    with open(f"{day}/{the_file}", "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.replace("\n", "").strip()
            if line == "":
                continue

        pass

    print(f"result: {}")


def part_two(test_only):
    print("=== Part Two ===")
    if test_only:
        the_file = "test_2.txt"
    else:
        the_file = "input.txt"
    print(f"file '{the_file}'")

    with open(f"{day}/{the_file}", "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.replace("\n", "").strip()
            if line == "":
                continue

        pass

    print(f"result: {}")


if __name__ == "__main__":
    part_one(True)
    # part_one(False)
    # part_two(True)
    # part_two(False)

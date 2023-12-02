import sys
import os
import re

sys.path.insert(0, os.path.abspath("."))
day = "01"


def part_1(test_only):
    print("=== Part One ===")
    if test_only:
        the_file = "test_1.txt"
    else:
        the_file = "input.txt"
    print(f"file '{the_file}'")

    pattern_first_digit = re.compile(r"[^\d]*(\d).*")
    pattern_last_digit = re.compile(r".*(\d)[^\d]*")

    total = 0

    with open(f"{day}/{the_file}", "r", encoding="utf-8") as input_file:
        line = input_file.readline().replace("\n", "")

        while line != "":
            first_digit = pattern_first_digit.findall(line)[0]
            last_digit = pattern_last_digit.findall(line)[0]
            total += int(first_digit + last_digit)
            line = input_file.readline().replace("\n", "")

    print(f"the total is {total}")

    print("result")


def digit_as_text_to_digit(digit_as_text):
    digit_as_text_list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    try:
        return str(digit_as_text_list.index(digit_as_text))
    except ValueError:
        return digit_as_text


def part_2(test_only):
    print("=== Part Two ===")
    if test_only:
        the_file = "test_2.txt"
    else:
        the_file = "input.txt"
    print(f"file '{the_file}'")

    pattern_first_digit = re.compile(
        r"[^(0|1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine)]*(0|1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine).*"
    )
    pattern_last_digit = re.compile(
        r".*(0|1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine)[^(0|1|2|3|4|5|6|7|8|9|0|one|two|three|four|five|six|seven|eight|nine)]*"
    )

    total = 0

    with open(f"{day}/{the_file}", "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.replace("\n", "").strip()
            if line == "":
                continue

            first_digit = digit_as_text_to_digit(pattern_first_digit.findall(line)[0])
            last_digit = digit_as_text_to_digit(pattern_last_digit.findall(line)[0])
            total += int(first_digit + last_digit)

    print(f"the total is {total}")

    print("result")


if __name__ == "__main__":
    part_1(True)
    part_1(False)
    part_2(True)
    part_2(False)

import sys
import os
import re
import numpy as np

sys.path.insert(0, os.path.abspath("."))


class BreakOutException(Exception):
    pass


class EngineSchematic:
    def __init__(self, schematic):
        self.schematic = schematic

    def is_symbol(self, row, col):
        if (
            row < 0
            or row >= len(self.schematic)
            or col < 0
            or col > len(self.schematic[0])
        ):
            return False
        return (not self.schematic[row][col].isdigit()) and (
            self.schematic[row][col] != "."
        )

    def is_asterisk(self, row, col):
        if (
            row < 0
            or row >= len(self.schematic)
            or col < 0
            or col > len(self.schematic[0])
        ):
            return False
        return self.schematic[row][col] == "*"


def parse_file(the_file):
    print(f"parsing '{the_file}'")
    with open(the_file, "r", encoding="utf-8") as input_file:
        line_list = input_file.readlines()

    return np.array([list(line.rstrip("\n")) for line in line_list])


def part_one(the_file):
    print("=== Part One ===")

    schematic = EngineSchematic(parse_file(the_file))

    total = 0

    parsing_number = False
    number_as_string = ""

    for row_index, row in enumerate(schematic.schematic):
        for col_index, char in enumerate(row):
            if char.isdigit():
                parsing_number = True
                number_as_string += char

            if parsing_number and (col_index == len(row) - 1 or not char.isdigit()):
                # working on a numner and reached end of row or non-digit character
                try:
                    for row_search_index in range(row_index - 1, row_index + 2):
                        for col_search_index in range(
                            col_index - len(number_as_string) - 1, col_index + 1
                        ):
                            if schematic.is_symbol(row_search_index, col_search_index):
                                total += int(number_as_string)
                                raise BreakOutException
                except BreakOutException:
                    pass
                parsing_number = False
                number_as_string = ""

    print(f"result: {total}")
    print()


def part_two(the_file):
    print("=== Part Two ===")
    schematic = EngineSchematic(parse_file(the_file))

    total = 0

    parsing_number = False
    number_as_string = ""
    asterisk_and_numbers_dict = dict()

    for row_index, row in enumerate(schematic.schematic):
        for col_index, char in enumerate(row):
            if char.isdigit():
                parsing_number = True
                number_as_string += char

            if parsing_number and (col_index == len(row) - 1 or not char.isdigit()):
                # working on a numner and reached end of row or non-digit character
                try:
                    for row_search_index in range(row_index - 1, row_index + 2):
                        for col_search_index in range(
                            col_index - len(number_as_string) - 1, col_index + 1
                        ):
                            if schematic.is_asterisk(
                                row_search_index, col_search_index
                            ):
                                key = (
                                    "r"
                                    + str(row_search_index)
                                    + "c"
                                    + str(col_search_index)
                                )
                                if key not in asterisk_and_numbers_dict:
                                    asterisk_and_numbers_dict[key] = list()
                                asterisk_and_numbers_dict[key].append(
                                    int(number_as_string)
                                )
                                raise BreakOutException
                except BreakOutException:
                    pass
                parsing_number = False
                number_as_string = ""

    for asterisk in asterisk_and_numbers_dict.values():
        if len(asterisk) == 2:
            total += asterisk[0] * asterisk[1]

    print(f"result: {total}")
    print()


if __name__ == "__main__":
    day = "03"
    # part_one(f"{day}/test_1.txt")
    # part_one(f"{day}/input.txt")
    part_two(f"{day}/test_1.txt")
    part_two(f"{day}/input.txt")

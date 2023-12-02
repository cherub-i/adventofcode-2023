import sys
import os
import re

sys.path.insert(0, os.path.abspath("."))


def parse_file(the_file):
    print(f"parsing '{the_file}'")
    game_list = list()

    pattern = re.compile(r"Game \d+: ([^;])+")

    with open(the_file, "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.replace("\n", "").strip()
            if line == "":
                continue

            cube_peek_list = list()

            line = re.sub("Game \d+: ", "", line)

            for cubes_peek_text in line.split("; "):
                cube_numbers = dict()

                for cube_peek_text in cubes_peek_text.split(", "):
                    cube_numbers[cube_peek_text.split(" ")[1]] = int(
                        cube_peek_text.split(" ")[0]
                    )

                new_cube_peek = cube_peek(
                    cube_numbers.get("red", 0),
                    cube_numbers.get("green", 0),
                    cube_numbers.get("blue", 0),
                )

                cube_peek_list.append(new_cube_peek)

            game_list.append(cube_peek_list)

    return game_list


def part_one(the_file):
    print("=== Part One ===")
    game_list = parse_file(the_file)

    print(f"result: {0}")


def part_two(the_file):
    print("=== Part Two ===")
    game_list = parse_file(the_file)

    print(f"result: {0}")


if __name__ == "__main__":
    day = "03"
    part_one(f"{day}/test_1.txt")
    # part_one(f"{day}/input.txt")
    # part_two(f"{day}/test_2.txt")
    # part_two(f"{day}/input.txt")

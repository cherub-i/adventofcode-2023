import sys
import os
import re
from dataclasses import dataclass

sys.path.insert(0, os.path.abspath("."))
day = "02"


@dataclass
class cube_peek:
    red: int
    green: int
    blue: int


def parse_file(the_file):
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


def part_one(test_only):
    print("=== Part One ===")
    if test_only:
        the_file = "test_1.txt"
    else:
        the_file = "input.txt"
    print(f"file '{the_file}'")

    game_list = parse_file(f"{day}/{the_file}")

    cubes_available = cube_peek(12, 13, 14)
    valid_games = list()

    for index, game in enumerate(game_list):
        valid_game = True
        for peek in game:
            if (
                peek.red > cubes_available.red
                or peek.green > cubes_available.green
                or peek.blue > cubes_available.blue
            ):
                valid_game = False

        if valid_game:
            valid_games.append(index + 1)

    print(f"result: {sum(valid_games)}")


def part_two(test_only):
    print("=== Part Two ===")
    if test_only:
        the_file = "test_1.txt"
    else:
        the_file = "input.txt"
    print(f"file '{the_file}'")

    game_list = parse_file(f"{day}/{the_file}")
    total = 0

    for game in game_list:
        cube_power = 0
        min_cubes = cube_peek(0, 0, 0)

        for peek in game:
            if peek.red > min_cubes.red:
                min_cubes.red = peek.red
            if peek.green > min_cubes.green:
                min_cubes.green = peek.green
            if peek.blue > min_cubes.blue:
                min_cubes.blue = peek.blue

        cube_power = min_cubes.red * min_cubes.green * min_cubes.blue
        total += cube_power

    print(f"result: {total}")


if __name__ == "__main__":
    part_one(True)
    part_one(False)
    part_two(True)
    part_two(False)

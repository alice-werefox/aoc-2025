#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> list[str]:
    grid: list[str] = []

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    for line in input_data:
        grid.append(line.strip())

    return grid


def is_accessessible(grid: list[str], row: int, col: int) -> bool:
    if grid[row][col] != "@":
        return False
    count = 0
    adjacent_spots = [[""] * 3] * 3
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if (
                row + x_offset < 0
                or row + x_offset > len(grid) - 1
                or col + y_offset < 0
                or col + y_offset > len(grid[0]) - 1
            ):
                continue
            adjacent_spots[x_offset + 1][y_offset + 1] = grid[row + x_offset][
                col + y_offset
            ]
            if grid[row + x_offset][col + y_offset] == "@":
                count += 1
    debug(f"ADJACENT SPOTS FOR {row}, {col}: {adjacent_spots}")
    return count < 4


def get_accessible_paper_rolls(grid: list[str]) -> int:
    count = 0
    for row in range(len(grid)):
        debug(f"CURRENT ROW: {grid[row]}")
        for col in range(len(grid[row])):
            debug(f"CURRENT VALUE: {grid[row][col]}")
            if is_accessessible(grid, row, col):
                count += 1
    return count


def main() -> None:
    input_filepath = "input/grid.txt"
    input_grid = parse_input(input_filepath)
    paper_rolls = get_accessible_paper_rolls(input_grid)
    print(f"Paper rolls accessible by the forklift: {paper_rolls}")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

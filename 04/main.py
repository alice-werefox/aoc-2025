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
    return count < 5


def get_accessible_paper_rolls(grid: list[str]) -> list[tuple[int, int, str]]:
    accessible_paper_rolls: list[tuple[int, int, str]] = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if is_accessessible(grid, row, col):
                accessible_paper_rolls.append((row, col, grid[row][col]))
    return accessible_paper_rolls


def remove_accessible_paper_rolls(
    current_grid: list[str], paper_rolls: list[tuple[int, int, str]]
) -> list[str]:
    for paper_roll in paper_rolls:
        current_grid[paper_roll[0]] = (
            current_grid[paper_roll[0]][: paper_roll[1]]
            + "x"
            + current_grid[paper_roll[0]][(paper_roll[1] + 1):]
        )
    debug("GRID AFTER REMOVALS:")
    for row in current_grid:
        debug(f"{row}")
    return current_grid


def main() -> None:
    input_filepath = "input/test_grid.txt"
    input_grid = parse_input(input_filepath)
    paper_rolls = get_accessible_paper_rolls(input_grid)
    count = len([x[2] for x in paper_rolls])
    print(f"Paper rolls initially accessible by the forklift: {count}")
    current_grid = input_grid
    remove_accessible_paper_rolls(current_grid, paper_rolls)
    while len(paper_rolls) > 0:
        paper_rolls = get_accessible_paper_rolls(current_grid)
        count += len([x[2] for x in paper_rolls])
        current_grid = remove_accessible_paper_rolls(current_grid, paper_rolls)
    print(f"Total paper rolls accessible by the forklift: {count}")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

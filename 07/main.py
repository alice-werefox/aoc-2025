#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv
from re import finditer


def parse_input(input_filepath: str) -> list[str]:

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    return [s.strip() for s in input_data]


def find_split_count(grid: list[str]) -> int:
    beams: set[int] = set([grid[0].find("S")])
    split_count = 0
    for row in grid[1:]:
        splitters: set[int] = set([i.start(0) for i in finditer("\\^", row)])
        if not splitters:
            debug(
                f"{"".join(list[str](map(lambda x: "|" if x in beams else ("^" if x in splitters else "."), range(len(grid)))))}"
            )
            continue
        intersections = beams.intersection(splitters)
        differences = beams.difference(splitters)
        split_count += len(intersections)
        beams = (
            set([x - 1 for x in intersections if x > 0])
            .union([x + 1 for x in intersections if x < len(grid) - 2])
            .union(differences)
            .difference(splitters)
        )
        debug(
            f"{"".join(list[str](map(lambda x: "|" if x in beams else ("^" if x in splitters else "."), range(len(grid)))))}"
        )
    return split_count


def main() -> None:
    input_filepath = "input/grid.txt"
    input_grid = parse_input(input_filepath)
    split_count = find_split_count(input_grid)
    print(f"The beam splits {split_count} times.")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

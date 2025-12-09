#!/usr/bin/env python3

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> list[tuple[int]]:
    output: tuple[list[tuple[int, int]], list[int]] = ([], [])

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    return [tuple([int(x) for x in line.strip().split(",") if x]) for line in input_data if line.strip()]


def main() -> None:
    input_filepath = "input/tiles.txt"
    input_tiles = parse_input(input_filepath)
    debug(input_tiles)
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

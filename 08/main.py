#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv
from math import sqrt


def parse_input(input_filepath: str) -> list[tuple[int, ...]]:

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"RAW INPUT: {input_data}")

    return [tuple(int(y) for y in x.split(",")) for x in input_data]


def get_distances(positions: list[tuple[int, ...]]) -> list[tuple[float, int, int]]:
    distances: list[tuple[float, int, int]] = []
    for a in range(len(positions)):
        for b in range(a + 1, len(positions)):
            distances.append(
                (
                    sqrt(
                        pow(positions[a][0] - positions[b][0], 2)
                        + pow(positions[a][1] - positions[b][1], 2)
                        + pow(positions[a][2] - positions[b][2], 2)
                    ),
                    a,
                    b,
                )
            )
    distances.sort(key=lambda x: x[0])
    return distances


def main() -> None:
    input_filepath = "input/test_junction_boxes.txt"
    junction_boxes = parse_input(input_filepath)
    distances = get_distances(junction_boxes)
    debug(f"DISTANCES BETWEEN BOXES: {distances}")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

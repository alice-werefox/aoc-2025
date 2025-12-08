#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv
from re import finditer


def parse_input(input_filepath: str) -> list[str]:

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    return [s.strip() for s in input_data]


def find_split_count_and_timelines(grid: list[str]) -> tuple[int, int]:
    beam_dict: dict = {grid[0].find("S"): 1}
    split_count: int = 0
    for row in range(len(grid[1:])):
        splitters: set[int] = set([i.start(0) for i in finditer("\\^", grid[row])])
        if not splitters:
            debug(
                f"{"".join(list[str](map(lambda x: "|" if (x in beam_dict.keys() and beam_dict[x] != 0) else ("^" if x in splitters else "."), range(len(grid)))))}"
            )
            continue
        intersections = set(
            [x for x in beam_dict.keys() if beam_dict[x] != 0]
        ).intersection(splitters)
        split_count += len(intersections)
        for i in intersections:
            temp_beams = beam_dict[i]
            beam_dict[i] = 0
            if (i - 1) in beam_dict.keys():
                beam_dict[i - 1] += temp_beams
            else:
                beam_dict[i - 1] = temp_beams
            if (i + 1) in beam_dict.keys():
                beam_dict[i + 1] += temp_beams
            else:
                beam_dict[i + 1] = temp_beams
        debug(
            f"{"".join(list[str](map(lambda x: "|" if (x in beam_dict.keys() and beam_dict[x]) else ("^" if x in splitters else "."), range(len(grid)))))}"
        )
    return (split_count, sum(beam_dict.values()))


def main() -> None:
    input_filepath = "input/grid.txt"
    grid = parse_input(input_filepath)
    split_count, timelines = find_split_count_and_timelines(grid)
    print(f"The beam splits {split_count} times.")
    print(f"There are {timelines} possible beam timelines.")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

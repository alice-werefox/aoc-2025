#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> tuple[list[tuple[int, int]], list[int]]:
    output: tuple[list[tuple[int, int]], list[int]] = ([], [])

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    ingredient_id = False
    for line in input_data:
        if line.strip() == "":
            ingredient_id = True
            continue
        if ingredient_id:
            output[1].append(int(line.strip()))
            continue
        output[0].append(
            (int(line.strip().split("-")[0]), int(line.strip().split("-")[1]))
        )

    return output


def find_available_fresh_ids(
    fresh_id_ranges: list[tuple[int, int]], available_ids: list[int]
) -> int:
    available_fresh_ids = 0

    for id in available_ids:
        for id_range in fresh_id_ranges:
            if id >= id_range[0] and id <= id_range[1]:
                available_fresh_ids += 1
                break

    return available_fresh_ids


def condense_id_ranges(id_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    id_ranges.sort(key=lambda id: id[0])
    debug(f"SORTED ID RANGES: {id_ranges}")
    condensed_ranges: list[tuple[int, int]] = []
    temp_range: tuple[int, int] = id_ranges[0]
    for i in range(1, len(id_ranges)):
        if temp_range[1] > id_ranges[i][1]:
            continue
        if temp_range[1] < id_ranges[i][0]:
            condensed_ranges.append(temp_range)
            temp_range = id_ranges[i]
            continue
        temp_range = (temp_range[0], id_ranges[i][1])
    condensed_ranges.append(temp_range)
    return condensed_ranges


def main() -> None:
    input_filepath = "input/ingredients.txt"
    input_fresh_ranges, input_available_ids = parse_input(input_filepath)
    debug(f"INPUT RANGES: {input_fresh_ranges}")
    debug(f"INPUT AVAILABLE IDS: {input_available_ids}")
    available_fresh_ids = find_available_fresh_ids(
        input_fresh_ranges, input_available_ids
    )
    debug(f"AVAILABLE FRESH IDS: {available_fresh_ids}")
    print(f"There are {available_fresh_ids} available fresh ingedients.")
    condensed_id_ranges = condense_id_ranges(input_fresh_ranges)
    debug(f"CONDENSESD RANGES: {condensed_id_ranges}")
    sum_of_id_ranges = sum([x[1] - x[0] + 1 for x in condensed_id_ranges])
    print(f"There are {sum_of_id_ranges} total fresh ingredient IDs.")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

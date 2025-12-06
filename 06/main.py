#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> tuple[list[list[int]], list[str]]:
    numbers: list[list[int]] = []
    operators: list[str] = []

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    for line in input_data:
        debug(f"\n\nRAW INPUT: {line}\n\n")

    for line in input_data:
        if "÷" == line.split()[0] or "*" == line.split()[0]:
            operators = line.split()
            break
        numbers.append([int(x) for x in line.split()])

    return (numbers, operators)


def main() -> None:
    input_filepath = "input/worksheet.txt"
    numbers, operators = parse_input(input_filepath)
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

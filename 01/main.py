#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> list[int]:
    rotations_list: list[int] = []

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    for line in input_data:
        rotation = line[0]
        amount = int(line[1:])
        if rotation == "L":
            rotations_list.append(0 - amount)
            continue
        rotations_list.append(amount)

    return rotations_list


def simulate_rotations(rotations_list: list[int]) -> list[int]:
    current_position = 50
    ending_positions: list[int] = []
    full_rotations = 0

    debug(f"\n\nROTATIONS LIST: {rotations_list}\n\n")

    for rotation in rotations_list:
        previous_position = current_position
        if rotation < 0:
            temp_rotation = abs(rotation) % 100
            current_position -= temp_rotation
        else:
            current_position += rotation % 100
        if current_position < 0:
            current_position += 100
            if previous_position != 0:
                full_rotations += 1
        elif current_position > 99:
            current_position -= 100
            if current_position != 0:
                full_rotations += 1
        full_rotations += int(abs(rotation) / 100)
        ending_positions.append(current_position)

    debug(f"\n\nENDING POSITIONS: {ending_positions}\n\n")

    zero_count = ending_positions.count(0)

    print(f"Simulated ending positions at zero: {zero_count}")

    return full_rotations + zero_count


def main() -> None:
    input_filepath = "input/rotations.txt"
    rotations_list = parse_input(input_filepath)
    password = simulate_rotations(rotations_list)
    print(f"The password is: {password}")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

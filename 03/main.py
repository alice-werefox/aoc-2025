#!/usr/bin/env python3

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> list[str]:
    battery_banks: list[str] = []

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    for line in input_data:
        battery_banks.append(line.strip())

    return battery_banks


def get_highest_joltage(battery_bank: str, digits: int) -> int:
    battery_list: list[tuple[str, int]] = [("0", -1)] * digits
    previous = 0

    for d in range(digits):
        for i in range(
            battery_list[previous][1] + 1, len(battery_bank) - (digits - d - 1)
        ):
            if int(battery_bank[i]) > int(battery_list[d][0]):
                battery_list[d] = (battery_bank[i], i)
        previous = d

    return int("".join([x[0] for x in battery_list]))


def get_highest_joltages(battery_banks: list[str], digits: int) -> list[int]:
    joltages: list[int] = []

    for battery_bank in battery_banks:
        joltages.append(get_highest_joltage(battery_bank, digits))

    return joltages


def main() -> None:
    input_filepath = "input/battery_banks.txt"
    input_battery_banks = parse_input(input_filepath)

    debug(f"\n\nPARSED BATTERY BANKS: {input_battery_banks}\n\n")

    digits = 2
    joltages = get_highest_joltages(input_battery_banks, digits)

    debug(f"\n\nJOLTAGES IDENTIFIED: {joltages}\n\n")
    print(f"Sum of joltages from {digits} batteries: {sum(joltages)}")

    digits = 12
    joltages = get_highest_joltages(input_battery_banks, digits)

    debug(f"\n\nJOLTAGES IDENTIFIED: {joltages}\n\n")
    print(f"Sum of joltages from {digits} batteries: {sum(joltages)}")

    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

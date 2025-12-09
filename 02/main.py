#!/usr/bin/env python3

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(input_filepath: str) -> list[tuple[int, int]]:
    ranges_list: list[tuple[int, int]] = []

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    # Should only be one line in the input.
    # In theory, this could be condensed to one line, but how about we don't.
    for line in input_data:
        split_line = line.split(",")
        for range in split_line:
            split_range = range.split("-")
            range_tuple: tuple[int, int] = (int(split_range[0]), int(split_range[1]))
            ranges_list.append(range_tuple)

    return ranges_list


def find_divisors_and_comparisons(
    product_id: int, repeats: int
) -> list[tuple[int, int]]:
    product_id_length = len(str(product_id))
    divisors = []
    if repeats != 0:
        if product_id_length % repeats == 0:
            divisor = int(product_id_length / repeats)
            divisors.append((divisor, product_id % pow(10, divisor)))
        return divisors
    for i in range(1, int(product_id_length / 2) + 1):
        if product_id_length % i == 0:
            divisors.append((i, product_id % pow(10, i)))
    return divisors


def select_bad_product_ids(
    input_ranges: list[tuple[int, int]], repeats: int
) -> set[int]:
    bad_product_ids = []
    for input_range in input_ranges:
        for product_id in range(input_range[0], input_range[1]):
            product_id_length = len(str(product_id))
            if repeats != 0:
                if product_id_length % repeats != 0:
                    continue
            divisors_and_comparisons = find_divisors_and_comparisons(
                product_id, repeats
            )
            debug(f"PRODUCT ID: {product_id}")
            debug(f"DIVISORS AND COMPARISONS: {divisors_and_comparisons}")
            for divisor_and_comparison in divisors_and_comparisons:
                current_product_id = product_id
                debug(f"CURRENT DIVISOR: {divisor_and_comparison[0]}")
                for i in range(int(product_id_length / divisor_and_comparison[0])):
                    debug(f"CURRENT PRODUCT ID ITERATION: {current_product_id}")
                    debug(f"CURRENT COMPARISON: {divisor_and_comparison[1]}")
                    iteration_modulus = current_product_id % pow(
                        10, divisor_and_comparison[0]
                    )
                    debug(f"ITERATION MODULUS: {iteration_modulus}")
                    if iteration_modulus != divisor_and_comparison[1]:
                        break
                    current_product_id = int(
                        current_product_id / pow(10, divisor_and_comparison[0])
                    )
                    if current_product_id == 0:
                        bad_product_ids.append(product_id)
            debug(f"BAD PRODUCT IDS: {bad_product_ids}\n")
    return set(bad_product_ids)


def main(repeats: int) -> None:
    input_filepath = "input/ranges.txt"
    input_ranges = parse_input(input_filepath)
    bad_product_ids = select_bad_product_ids(input_ranges, repeats)
    print(bad_product_ids)
    print(sum(bad_product_ids))
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    if "-t" in argv or "--twice" in argv:
        main(2)
    else:
        main(0)
    exit(0)

#!/bin/python

from logging import debug, DEBUG, basicConfig
from sys import argv


def parse_input(
    input_filepath: str,
) -> tuple[list[tuple[list[int], str]], list[tuple[list[int], str]]]:
    numbers: list[str] = []
    operators: str = ""

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    for line in input_data:
        if line.find("+") != -1:
            operators = line
            break
        numbers.append(line)

    human_math: list[tuple[list[int], str]] = [
        ([int(n.split()[o]) for n in numbers], operators.split()[o])
        for o in range(len(operators.split()))
    ]

    cephalapod_math: list[tuple[list[int], str]] = translate_input(numbers, operators)

    return (human_math, cephalapod_math)


def translate_input(numbers: list[str], operators: str) -> list[tuple[list[int], str]]:
    cephalapod_math: list[tuple[list[int], str]] = []
    current_numbers: list[int] = []
    current_operator = operators[0]

    for i in range(len(operators)):
        if operators[i] in ["+", "*"] and current_numbers != []:
            cephalapod_math.append((current_numbers, current_operator))
            current_operator = operators[i]
            current_numbers = []
        temp_number: str = ""
        for row in numbers:
            temp_number += row[i].strip()
        if temp_number != "":
            current_numbers.append(int(temp_number))
    cephalapod_math.append((current_numbers, current_operator))

    return cephalapod_math


def get_solutions(math_problems: list[tuple[list[int], str]]) -> list[int]:
    debug(f"PROBLEMS: {math_problems}")
    solutions: list[int] = []
    for problem in math_problems:
        if problem[1] == "+":
            solutions.append(sum(problem[0]))
            continue
        product = problem[0][0]
        for n in problem[0][1:]:
            product *= n
        solutions.append(product)
    debug(f"SOLUTIONS: {solutions}")
    return solutions


def main() -> None:
    input_filepath = "input/worksheet.txt"
    human_math, cephalapod_math = parse_input(input_filepath)
    solutions = get_solutions(human_math)
    print(f"Sum of all (human math) solutions: {sum(solutions)}")
    solutions = get_solutions(cephalapod_math)
    print(f"Sum of all (cephalapod math) solutions: {sum(solutions)}")
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

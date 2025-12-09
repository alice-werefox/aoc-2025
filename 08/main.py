#!/usr/bin/env python3

from logging import debug, DEBUG, basicConfig
from sys import argv


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
                    pow(positions[a][0] - positions[b][0], 2)
                    + pow(positions[a][1] - positions[b][1], 2)
                    + pow(positions[a][2] - positions[b][2], 2),
                    a,
                    b,
                )
            )
    distances.sort(key=lambda x: x[0])
    return distances


def create_circuits(
    distances: list[tuple[float, int, int]], n: int
) -> tuple[list[int], tuple[float, int, int]]:
    single_circuits: list[int] = [x for x in range(n)]
    circuits: list[set[int]] = []
    count = 0
    circuits_after_n: list[int] = []
    for d in distances:
        if count == 999:
            circuits_after_n = [len(x) for x in circuits]
        if len(single_circuits) == 0 and len(circuits) == 1:
            break
        count += 1
        debug(f"Current Iteration: {count} | {d} | {circuits}")
        a_in_single_circuits = d[1] in single_circuits
        b_in_single_circuits = d[2] in single_circuits
        if a_in_single_circuits or b_in_single_circuits:
            if a_in_single_circuits and b_in_single_circuits:
                circuits.append(set([d[1], d[2]]))
                single_circuits.remove(d[1])
                single_circuits.remove(d[2])
                continue
            for c in circuits:
                if d[1] in c:
                    c.add(d[2])
                    single_circuits.remove(d[2])
                    break
                if d[2] in c:
                    c.add(d[1])
                    single_circuits.remove(d[1])
                    break
            continue
        circuit_a = circuit_b = set()
        for c in circuits:
            if d[1] in c:
                circuit_a = c
            if d[2] in c:
                circuit_b = c
        if circuit_a == circuit_b:
            continue
        circuits.remove(circuit_a)
        circuits.remove(circuit_b)
        circuits.append(circuit_a.union(circuit_b))
    return (circuits_after_n, distances[count - 1])


def main() -> None:
    input_filepath = "input/junction_boxes.txt"
    junction_boxes = parse_input(input_filepath)
    distances = get_distances(junction_boxes)
    debug(f"DISTANCES BETWEEN BOXES: {distances}")
    circuits_after_n, final_distance = create_circuits(distances, len(junction_boxes))
    debug(f"CIRCUITS CREATED AFTER 1000 ITERATIONS: {circuits_after_n}")
    debug(
        f"FINAL DISTANCE EXAMINED: {final_distance[0]} | {junction_boxes[final_distance[1]]} | {junction_boxes[final_distance[2]]}"
    )
    circuits_after_n.sort(reverse=True)
    product_of_n_largest_circuits = (
        circuits_after_n[0] * circuits_after_n[1] * circuits_after_n[2]
    )
    print(
        f"The product of the three largest circuits after 1000 iterations is: {product_of_n_largest_circuits}"
    )
    print(
        f"The product of the x coordinates of the last two junction boxes connected: {junction_boxes[final_distance[1]][0] * junction_boxes[final_distance[2]][0]}"
    )
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

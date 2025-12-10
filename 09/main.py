#!/usr/bin/env python3

from logging import debug, DEBUG, basicConfig
from sys import argv

# from math import dist


def parse_input(input_filepath: str) -> list[tuple[int, int]]:

    with open(file=input_filepath, mode="r") as input_file:
        input_data: list[str] = input_file.readlines()

    debug(f"\n\nRAW INPUT: {input_data}\n\n")

    return [
        (int(line.strip().split(",")[0]), int(line.strip().split(",")[1]))
        for line in input_data
        if line.strip()
    ]


def find_areas(
    coordinate_pairs: list[tuple[int, int]],
) -> list[tuple[int, int, int]]:
    areas: list[tuple[int, int, int]] = []

    for c in range(len(coordinate_pairs)):
        for d in range(c + 1, len(coordinate_pairs)):
            areas.append(
                (
                    (abs((coordinate_pairs[c][0] - coordinate_pairs[d][0])) + 1)
                    * (abs(coordinate_pairs[c][1] - coordinate_pairs[d][1]) + 1),
                    c,
                    d,
                )
            )

    return areas


# 4616586187
def find_within_bounds(
    rectangles: list[tuple[int, int, int]], vertices: list[tuple[int, int]]
) -> tuple[int, int, int]:
    for r in rectangles:
        contains_vertices = False
        min_x = min(vertices[r[1]][0], vertices[r[2]][0])
        min_y = min(vertices[r[1]][1], vertices[r[2]][1])
        max_x = max(vertices[r[1]][0], vertices[r[2]][0])
        max_y = max(vertices[r[1]][1], vertices[r[2]][1])
        debug(f"{r[0]}, {vertices[r[1]]}, {vertices[r[2]]}")
        in_x_bounds = vertices[0][0] > min_x and vertices[0][0] < max_x
        in_y_bounds = vertices[0][1] > min_y and vertices[0][1] < max_y
        if in_x_bounds and in_y_bounds:
            debug(f"{vertices[0]}")
            continue
        scanline_x_max = []
        scanline_x_min = []
        scanline_y_max = []
        scanline_y_min = []
        for v in range(len(vertices[1:])):
            in_x_bounds = vertices[v][0] > min_x and vertices[v][0] < max_x
            in_y_bounds = vertices[v][1] > min_y and vertices[v][1] < max_y
            if in_x_bounds and in_y_bounds:
                debug(f"{v}")
                contains_vertices = True
                break
            if (
                max(vertices[v][1], vertices[v - 1][1]) >= max_y
                and min(vertices[v][1], vertices[v - 1][1]) <= max_y
            ):
                scanline_y_max.append(vertices[v][0])
            if (
                max(vertices[v][1], vertices[v - 1][1]) >= min_y
                and min(vertices[v][1], vertices[v - 1][1]) <= min_y
            ):
                scanline_y_min.append(vertices[v][0])
            if (
                max(vertices[v][0], vertices[v - 1][0]) >= max_x
                and min(vertices[v][0], vertices[v - 1][0]) <= max_x
            ):
                scanline_x_max.append(vertices[v][1])
            if (
                max(vertices[v][0], vertices[v - 1][0]) >= min_x
                and min(vertices[v][0], vertices[v - 1][0]) <= min_x
            ):
                scanline_x_min.append(vertices[v][1])
        if contains_vertices:
            continue
        scanline_x_min = [x for x in set(scanline_x_min)]
        scanline_x_max = [x for x in set(scanline_x_max)]
        scanline_y_min = [x for x in set(scanline_y_min)]
        scanline_y_max = [x for x in set(scanline_y_max)]
        scanline_x_min.sort()
        scanline_x_max.sort()
        scanline_y_min.sort()
        scanline_y_max.sort()
        debug(
            f"\n{scanline_x_min}\n{scanline_x_max}\n{scanline_y_min}\n{scanline_y_max}"
        )
        for x in range(len(scanline_y_min)):
            if scanline_y_min[x] > max_x and x % 2 == 0:
                break
        for x in range(len(scanline_y_max)):
            if scanline_y_max[x] > max_x and x % 2 == 0:
                break
        for y in range(len(scanline_x_min)):
            if scanline_x_min[y] > max_y and y % 2 == 0:
                break
        for y in range(len(scanline_x_max)):
            if scanline_x_max[y] > max_y and y % 2 == 0:
                break
        return r
    return (0, 0, 0)


def main() -> None:
    input_filepath = "input/tiles.txt"
    input_tiles = parse_input(input_filepath)
    areas = find_areas(input_tiles)
    debug(areas)
    areas.sort(key=lambda x: x[0], reverse=True)
    debug(areas)
    print(f"The largest area you can make is: {areas[0][0]}")
    print(
        f"The largest area you can make within bounds: {find_within_bounds(areas, input_tiles)[0]}"
    )
    return


if __name__ == "__main__":
    if "-d" in argv or "--debug" in argv:
        basicConfig(filename="debug.log", level=DEBUG)
    main()
    exit(0)

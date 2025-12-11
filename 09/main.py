#!/usr/bin/env python3

from logging import debug, DEBUG, basicConfig
from sys import argv
from shapely.geometry.polygon import Polygon


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


# def find_within_bounds(
#     rectangles: list[tuple[int, int, int]], vertices: list[tuple[int, int]]
# ) -> tuple[int, int, int]:
#     for r in rectangles:
#         outside_bounds = False
#         min_x = min(vertices[r[1]][0], vertices[r[2]][0])
#         max_x = max(vertices[r[1]][0], vertices[r[2]][0])
#         min_y = min(vertices[r[1]][1], vertices[r[2]][1])
#         max_y = max(vertices[r[1]][1], vertices[r[2]][1])
#         debug(f"{r[0]}, {vertices[r[1]]}, {vertices[r[2]]}")
#         left_intersects = -1
#         right_intersects = -1
#         down_intersects = -1
#         up_intersects = -1
#         for v in range(len(vertices[1:])):
#             is_horizontal_line = vertices[v - 1][1] == vertices[v][1]
#             is_vertical_line = vertices[v - 1][0] == vertices[v][0]
#             is_in_y_bounds = vertices[v][1] > min_y and vertices[v][1] < max_y
#             is_in_x_bounds = vertices[v][0] > min_x and vertices[v][0] < max_x
#             line_intersects_left = (
#                 min(vertices[v - 1][0], vertices[v][0]) < min_x
#                 and max(vertices[v - 1][0], vertices[v][0]) > min_x
#             )
#             line_intersects_right = (
#                 min(vertices[v - 1][0], vertices[v][0]) < max_x
#                 and max(vertices[v - 1][0], vertices[v][0]) > max_x
#             )
#             line_intersects_down = (
#                 min(vertices[v - 1][1], vertices[v][1]) < min_y
#                 and max(vertices[v - 1][1], vertices[v][1]) > min_y
#             )
#             line_intersects_up = (
#                 min(vertices[v - 1][1], vertices[v][1]) < max_y
#                 and max(vertices[v - 1][1], vertices[v][1]) > max_y
#             )

#             if is_horizontal_line:
#                 if line_intersects_left or line_intersects_right:
#                     if is_in_y_bounds:
#                         debug(f"{vertices[v-1]}, {vertices[v]}")
#                         outside_bounds = True
#                         break
#                 if line_intersects_left:
#                     left_intersects += 1
#                 if line_intersects_right:
#                     right_intersects += 1

#             if is_vertical_line:
#                 if line_intersects_down or line_intersects_up:
#                     if is_in_x_bounds:
#                         debug(f"{vertices[v-1]}, {vertices[v]}")
#                         outside_bounds = True
#                         break
#                 if line_intersects_down:
#                     down_intersects += 1
#                 if line_intersects_up:
#                     up_intersects += 1

#         if (
#             outside_bounds
#             or (
#                 left_intersects < 0
#                 or right_intersects < 0
#                 or down_intersects < 0
#                 or up_intersects < 0
#             )
#             or (
#                 left_intersects % 2 == 1
#                 or right_intersects % 2 == 1
#                 or down_intersects % 2 == 1
#                 or up_intersects % 2 == 1
#             )
#         ):
#             continue

#         return r

#     return (0, 0, 0)


def find_within_bounds(
    rectangles: list[tuple[int, int, int]], vertices: list[tuple[int, int]]
) -> tuple[int, int, int]:
    tile_shape = Polygon(vertices)
    for r in rectangles:
        area = Polygon(
            [
                vertices[r[1]],
                (vertices[r[1]][0], vertices[r[2]][1]),
                vertices[r[2]],
                (vertices[r[2]][0], vertices[r[1]][1]),
            ]
        )
        if tile_shape.contains(area):
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

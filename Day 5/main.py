
from collections import Counter
import pandas as pd
import numpy as np


def get_start_coord(lst: list):
    start = lst[0].split(',')
    start_x = int(start[0])
    start_y = int(start[1])
    return [start_x, start_y]


def get_end_coord(lst: list):
    ending = lst[1].split(',')
    end_x = int(ending[0])
    end_y = int(ending[1])
    return [end_x, end_y]


def check_orientation(start: list, end: list):
    if start[0] == end[0]:
        return 'v'
    elif start[1] == end[1]:
        return 'h'
    return 'd'


def sort_coord_pt(a: int, b: int):
    if a > b:
        return [b, a]
    return [a, b]


def get_paired_list(xy_coord: list):
    paired_list = []
    for i in range(0, len(xy_coord[0])):
        paired_list.append([xy_coord[0][i], xy_coord[1][i]])

    return paired_list


def get_directions(x1, x2, y1, y2):
    if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
        x_val_sorted = sort_coord_pt(x1, x2)
        y_val_sorted = sort_coord_pt(y1, y2)
        x_vals = [*range(x_val_sorted[0], x_val_sorted[1]+1)]
        y_vals = [*range(y_val_sorted[0], y_val_sorted[1]+1)]
    elif x1 > x2:
        x_vals = [*range(x1, x2-1, -1)]
        y_vals = [*range(y1, y2+1)]
    elif y1 > y2:
        x_vals = [*range(x1, x2+1)]
        y_vals = [*range(y1, y2-1, -1)]
    return x_vals, y_vals


def get_diagonal_coords(start: list, end: list):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    x_vals, y_vals = get_directions(x1, x2, y1, y2)

    return x_vals, y_vals


def get_line_coord(list_coord):
    starting = get_start_coord(list_coord)
    ending = get_end_coord(list_coord)
    ori = check_orientation(starting, ending)
    if ori == 'v':
        y_coord_sort = sort_coord_pt(starting[1], ending[1])
        y_coord = [*range(y_coord_sort[0], y_coord_sort[1]+1)]
        x_coord = [starting[0]]*len(y_coord)
    elif ori == 'h':
        x_coord_sorted = sort_coord_pt(starting[0], ending[0])
        x_coord = [*range(x_coord_sorted[0], x_coord_sorted[1]+1)]
        y_coord = [starting[1]]*len(x_coord)
    elif ori == 'd':
        x_coord, y_coord = get_diagonal_coords(starting, ending)

    return get_paired_list([x_coord, y_coord])


datalines = []
with open(r"Day 5\test_data.txt") as data:
    for line in data:
        striped_line = line.rstrip()
        datalines.append(striped_line.split(' -> '))


def get_all_vent_coord(datalines):
    vents = []
    for coord in datalines:
        vent_coord = get_line_coord(coord)
        if not isinstance(vent_coord, bool):
            # print(vent_coord)
            vents += vent_coord
    return vents


vent_coord = get_all_vent_coord(datalines)

tuple_vent_coord = map(tuple, vent_coord)
coord_count = Counter(tuple_vent_coord)
counts = list(coord_count.values())

coord_gt_1 = [i for i in counts if i > 1]
print(len(coord_gt_1))

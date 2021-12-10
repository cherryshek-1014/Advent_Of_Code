from types import GetSetDescriptorType
from corners import check_all_corners
from map_functions import get_shape
from edges import check_edges
from remainder import check_all_remaining

with open(r'C:\Users\Cherry\Desktop\Programming\Advent_Of_Code\Day 9\test_data.txt') as file:
    data = []
    for f in file:
        f = f.rstrip()
        data.append([int(i) for i in f])


def run_all(data: list) -> int:
    map_shape = get_shape(data)

    corner_total = check_all_corners(data, map_shape)
    edges = check_edges(data, map_shape)
    remainder = check_all_remaining(data, map_shape)

    return edges


print(run_all(data))

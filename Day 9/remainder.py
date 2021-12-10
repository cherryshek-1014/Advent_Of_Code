from map_functions import check_pts


def get_remain_coord(data: list, shape: list) -> list:
    return [[i, j] for i in range(1, shape[1]-1) for j in range(1, shape[0]-1)]


def get_adj_coord(coord: list):
    row = coord[0]
    col = coord[1]
    return [[row, col+1], [row, col-1], [row-1, col], [row+1, col]]


def check_all_remaining(data: list, shape: list) -> int:
    coords = get_remain_coord(data, shape)
    total = 0
    for coord in coords:
        coord_to_check = get_adj_coord(coord)
        if check_pts(data, coord, coord_to_check):
            total = total + data[coord[0]][coord[1]] + 1
    return total

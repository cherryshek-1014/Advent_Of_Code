from map_functions import check_pts


def get_edge_coord(data: list, shape: list) -> dict:
    top_coord = [[0, i] for i in range(1, shape[0]-1)]
    bot_coord = [[shape[1]-1, i] for i in range(1, shape[0]-1)]
    rhs_coord = [[i, shape[0]-1] for i in range(1, shape[1]-1)]
    lhs_coord = [[i, 0] for i in range(1, shape[1]-1)]
    return {'top': top_coord, 'bot': bot_coord, 'right': rhs_coord, 'left': lhs_coord}


def get_check_pts_top(coord: list) -> list:
    return [[coord[0], coord[1]-1], [coord[0], coord[1]+1], [coord[0]+1, coord[1]]]


def get_check_pts_bot(coord: list) -> list:
    return [[coord[0], coord[1]-1], [coord[0], coord[1]+1], [coord[0]-1, coord[1]]]


def get_check_pts_right(coord: list) -> list:
    return [[coord[0]-1, coord[1]], [coord[0]-1, coord[1]], [coord[0], coord[1]-1]]


def get_check_pts_left(coord: list) -> list:
    return [[coord[0]-1, coord[1]], [coord[0]+1, coord[1]], [coord[0], coord[1]+1]]


def check_edges(data: list, shape: list):
    edge_coord = get_edge_coord(data, shape)
    edges = {
        'top': {'coords': edge_coord['top'], 'check': get_check_pts_top},
        'bot': {'coords': edge_coord['bot'], 'check': get_check_pts_bot},
        'right': {'coords': edge_coord['right'], 'check': get_check_pts_right},
        'left': {'coords': edge_coord['left'], 'check': get_check_pts_left}
    }
    total = 0
    for key, val in edges.items():
        pts = val['coords']
        for pt in pts:
            coord_to_check = val['check'](pt)
            if check_pts(data, pt, coord_to_check):
                total = total + (data[pt[0]][pt[1]] + 1)
    print(edge_coord)
    return total

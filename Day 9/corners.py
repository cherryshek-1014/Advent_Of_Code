
from map_functions import check_pts


def get_corner_coords(shape: list) -> dict:
    corners = {
        'top_left': {'coord': [0, 0],
                     'check': [[0, 1], [1, 0]]},
        'top_right': {'coord': [0, shape[0]-1],
                      'check': [[0, shape[0]-2], [1, shape[0]-1]]},
        'bot_left': {'coord': [shape[1]-1, 0],
                     'check': [[shape[1]-1, 1], [shape[1]-2, 0]]},
        'bot_right': {'coord': [shape[1]-1, shape[0]-1],
                      'check': [[shape[1]-1, shape[0]-2], [shape[1]-2, shape[0]-1]]}
    }
    return corners


def check_all_corners(data: list, shape: list):
    corners = get_corner_coords(shape)
    total = 0
    for key, corner in corners.items():
        if check_pts(data, corner['coord'], corner['check']):
            total = total + data[corner['coord'][0]][corner['coord'][1]] + 1
    print(corners)
    return total

def get_shape(data: list) -> list:
    return [len(data[0]), len(data)]


def check_pts(data: list, pt: list, border_pts: list) -> bool:
    for pts in border_pts:
        #       if data[pt[0]][pt[1]] == 9:
        #            return False

        if data[pt[0]][pt[1]] > data[pts[0]][pts[1]]:
            return False

    # print(pt)
    return True

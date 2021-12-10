def isLowPoint(row, column, grid):
    """This function is used to determine if a given map location is a low point.
    This is done by obtaining first the indexes of the adjacent horizontal grid positions, then
    filtering them to ensure they are inside the grid (index must be greater than 0, less than the max row/col
    dimension).  The values for each neighbor are then obtained and the min value is compared to the value at the
    current grid location."""
    max_row = len(grid)
    max_col = len(grid[0])
    current_location_value = grid[row][column]
    possible_neighbors = []
    # populate the (row, col) of all adjacent locations - no diagonals though
    for i in (row - 1, row + 1):
        possible_neighbors.append((i, column))
    for j in (column - 1, column + 1):
        possible_neighbors.append((row, j))
    # x below is a (row, col) tuple for neighbors around the location in question
    # filter is used to avoid IndexErrors from going outside the matrix edges
    neighbors = list(filter(
        lambda x: 0 <= x[0] < max_row and 0 <= x[1] < max_col, possible_neighbors))
    neighbor_values = [grid[y][x] for (y, x) in neighbors]
    return current_location_value < min(neighbor_values)


def part1(hmap):
    total_risk = 0
    # keep track of the low points
    lowpoints = []
    for i, row in enumerate(hmap):
        for j, col in enumerate(row):
            if isLowPoint(i, j, hmap):
                lowpoints.append((i, j))
                # risk value of a low point is 1 plus its height
                total_risk += (1 + col)
    return total_risk, lowpoints


if __name__ == '__main__':
    FILENAME = r'C:\Users\Cherry\Desktop\Programming\Advent_Of_Code\Day 9\test_data.txt'
    with open(FILENAME) as f:
        lines = f.readlines()
        heightmap = [[int(x) for x in row if x.isdigit()] for row in lines]

    risk, low = part1(heightmap)
    print(risk)

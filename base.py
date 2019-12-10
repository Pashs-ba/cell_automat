import numpy as np

size_y = 50
size_x = 50
cell = [[0, 1, 0], 1]
hole = np.array([[cell for i in range(50)] for j in range(50)])
hole[1, 3] = 1
start_hole = hole.copy()


def find_neighbors(x, y, mod_x, mod_y, hole):
    try:
        if bool(hole[y+mod_y, x+mod_x]):
            return 1
        else:
            return 0

    except IndexError:
        return 0


def condition(a, cell):
    if a == 3:
        return 2
    elif (a == 2 or a == 3) and cell != 0:
        return 1
    else:
        return 0


def next_motion(hole):
    new_hole = hole.copy()
    for x in range(size_x-1):
        for y in range(size_y-1):
            neighbors = np.array([find_neighbors(*(x, y), 1, 0, hole),
                                  find_neighbors(*(x, y), 0, 1, hole),
                                  find_neighbors(*(x, y), -1, 0, hole),
                                  find_neighbors(*(x, y), 0, -1, hole),
                                  find_neighbors(*(x, y), 1, -1, hole),
                                  find_neighbors(*(x, y), 1, 1, hole),
                                  find_neighbors(*(x, y), -1, -1, hole),
                                  find_neighbors(*(x, y), -1, 1, hole)])
            a = neighbors.sum()
            new_hole[y, x] = condition(a, new_hole[y, x])
    return new_hole


if __name__ == '__main__':
    for i in hole:
        print(i)
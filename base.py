import numpy as np
import random
size_y = 50
size_x = 50
hole = np.zeros((size_y, size_x), 'uint8')
hole[1, 3] = 1
hole[2, 3] = 1
hole[3, 3] = 1
hole[3, 2] = 1
hole[2, 1] = 1
start_hole = hole.copy()
def find_neighbors(x, y, mod_x, mod_y, hole):
    try:
        return hole[y+mod_y, x+mod_x]
    except IndexError:
        return 0


def next_motion(hole):
    new_hole = hole.copy()
    for x in range(size_x-1):
        for y in range(size_y-1):
            # print(x, y)
            coor = (x, y)
            neighbors = np.array([find_neighbors(*coor, 1, 0, hole),
                         find_neighbors(*coor, 0, 1, hole),
                         find_neighbors(*coor, -1, 0, hole),
                         find_neighbors(*coor, 0, -1, hole),
                         find_neighbors(*coor, 1, -1, hole),
                         find_neighbors(*coor, 1, 1, hole),
                         find_neighbors(*coor, -1, -1, hole),
                         find_neighbors(*coor, -1, 1, hole)])
            a = neighbors.sum()
            # if x == 1 and y == 1:
            #     print(neighbors)
            #     print(hole[y, x])
            #     exit()
            if a == 3:
                new_hole[y, x] = 1
            elif (a == 2 or a == 3) and hole[y, x] == 1:
                # print('hello')
                new_hole[y, x] = 1
            else:
                new_hole[y, x] = 0
    return new_hole


if __name__ == '__main__':
    for i in range(1000):
        hole = next_motion(hole)
        print(hole)

import sys
import numpy as np


def load_points(path) -> np.array:
    with open(path) as file:
        contents = file.read().replace("->", ",").replace("\n", ",")
        array = np.fromstring(contents, sep=",", dtype="uint")
        return array.reshape(int(array.size/4), 2, 2)


def part1(path):
    points = load_points(path)
    straight_lines = points[np.where((points[:,0] - points[:,1]) == 0)[0]]
    max_number = straight_lines.max()
    board = np.zeros((max_number+1, max_number+1), dtype='uint')
    for pair in straight_lines:
        xs = pair[:,0]
        ys = pair[:,1]
        xs.sort()
        ys.sort()
        for x in range(xs[0], xs[1] + 1):
            for y in range(ys[0], ys[1] + 1):
                board[x,y] +=1
    print(board)
    return np.where(board >= 2)[0].size

if __name__ == "__main__":
    print(f"{part1(sys.argv[1])} 2 lines overlap")

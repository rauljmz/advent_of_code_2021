import sys
import numpy as np


def load_points(path) -> np.array:
    with open(path) as file:
        contents = file.read().replace("->", ",").replace("\n", ",")
        array = np.fromstring(contents, sep=",", dtype="int")
        return array.reshape(int(array.size/4), 2, 2)


def number_of_line_crosses(board):
    return np.where(board >= 2)[0].size


def create_board_for(points):
    max_number = points.max()
    return np.zeros((max_number+1, max_number+1), dtype='uint')


def mark_points_on_board(points):
    board = create_board_for(points)
    for pair_of_points in points:
        increment = pair_of_points[1] - pair_of_points[0]
        no_points_in_line = np.absolute(increment).max() + 1
        step = (increment / (no_points_in_line-1)).astype('int')
        for line_point in range(no_points_in_line):
            board[tuple(pair_of_points[0]+(step*line_point))] += 1
    return board


def part1(path):
    points = load_points(path)
    straight_lines = points[np.where((points[:, 0] - points[:, 1]) == 0)[0]]
    board = mark_points_on_board(straight_lines)
    print(board)
    return number_of_line_crosses(board)


def part2(path):
    points = load_points(path)
    board = mark_points_on_board(points)
    print(board)
    return number_of_line_crosses(board)


if __name__ == "__main__":
    print(f"{part2(sys.argv[1])} 2 lines overlap")

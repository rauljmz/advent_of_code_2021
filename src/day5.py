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
    increments = points[:,1] - points[:,0]
    for index in range(points.shape[0]):
        no_points_in_line = np.absolute(increments[index]).max()
        step = (increments[index] / no_points_in_line).astype('int')
        for line_point in range(no_points_in_line + 1):
            board[
                points[index,0,0]+step[0]*line_point,
                points[index,0,1]+step[1]*line_point,
                ] +=1
    return board

def part1(path):
    points = load_points(path)
    straight_lines = points[np.where((points[:,0] - points[:,1]) == 0)[0]]
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

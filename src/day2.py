import sys
import numpy as np
from functools import reduce

moves = {
    "forward": (1,1,0),
    "up": (0,0,-1),
    "down": (0,0,1),
}

def move(position, step):
    move = np.array(moves.get(step[0]))
    count = step[1]
    current_aim = position[2]
    return position + move * np.array([count,count*current_aim,count])

def main(path):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            (direction, count) = line.split(" ")
            data.append((direction, int(count)))

    final_position = reduce(move, data, np.array([0,0,0]))[:2]
    return np.prod(final_position)

if __name__ == "__main__":
    print(f"{main(sys.argv[1])} result of multiplying position")
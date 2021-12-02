import sys
import numpy as np
from functools import reduce 

moves = {
    "forward": (1,0),
    "up": (0,-1),
    "down": (0,1),
}

def move(position, step):
    return position + (np.array(moves.get(step[0])) * step[1])

def main(path):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            (direction, count) = line.split(" ")
            data.append((direction, int(count)))
    return np.prod(reduce(move, data, np.array([0,0])))

if __name__ == "__main__":
    print(f"{main(sys.argv[1])} result of multiplying position")
import sys
import numpy as np


def load_data(path) -> np.array:
    return np.fromfile(path, sep=",", dtype='int')


def part1(path):
    positions = load_data(path)
    median = np.median(positions)
    movements = np.absolute((positions - median))
    return int(movements.sum())


if __name__ == "__main__":
    print(f"Minimum fuel {part1(sys.argv[1])}")

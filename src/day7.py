import sys
import numpy as np


def load_data(path) -> np.array:
    return np.fromfile(path, sep=",", dtype='int')


def part1(path):
    positions = load_data(path)
    median = np.median(positions)
    movements = np.absolute((positions - median))
    return int(movements.sum())


def fuel_cost(steps):
    return np.arange(steps+1).sum()


def part2(path):
    positions = load_data(path)
    mean = int(positions.mean())
    movements = np.absolute(
        (positions - np.arange(mean, mean+2)[:, np.newaxis])
    )
    fn = np.vectorize(fuel_cost)
    return fn(movements).sum(axis=1).min()


if __name__ == "__main__":
    print(f"Minimum fuel {part2(sys.argv[1])}")

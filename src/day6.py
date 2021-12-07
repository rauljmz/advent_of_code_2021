import sys
import numpy as np


def count_from_single_fish(initial, days):
    count = 1
    for reproduction_day in range(initial + 1, days + 1, 7):
        count += count_from_single_fish(8, days-reproduction_day)
    return count


def count_fish(path, days):
    with open(path) as file:
        initial_states = np.fromstring(file.readline(), sep=',', dtype=np.uint)

    fn = np.frompyfunc(count_from_single_fish, 2, 1)
    return fn(initial_states, days).sum()


def part1(path):
    return count_fish(path, 80)


if __name__ == "__main__":
    print(f"{part1(sys.argv[1])} fish")

import sys
import numpy as np


def load_data(path) -> np.array:
    with open(path) as file:
        lines_array = file.read().replace(' | ', ' ').replace('\n', ' ').split(' ')
    array = np.fromiter(lines_array, "S8")
    return array.reshape(int(array.size/14), 14)


def part1(path):
    data = load_data(path)
    digits = data[:, 10:]
    lengths = np.char.str_len(digits)
    return lengths[np.isin(lengths, [2, 3, 4, 7])].size



if __name__ == "__main__":
    print(f"{part1(sys.argv[1])} digits")

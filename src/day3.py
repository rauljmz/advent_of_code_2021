import sys
import numpy as np


def read_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            digits = [int(digit) for digit in list(line.strip())]
            data.append(digits)
    return np.array(data)


def to_decimal(arr):
    to_decimal_array = 2 ** np.arange(len(arr)-1, -1, -1)
    return (arr*to_decimal_array).sum()


def most_common_digit(np_array: np.array):
    """Returns the most common digit in a binary array
        If the number of 0s and 1s is the same, it returns 1

        It uses floor instead of round, because round 
        goes to the nearest even number in case of being halfway
        e.g. round(0.5) == 0 and round(1.5) == 2
    """
    return np.floor(np_array.mean(axis=0) + 0.5).astype('int')


def least_common_digit(np_array: np.array):
    return most_common_digit(np_array) ^ True


def part1(path):
    data = read_data(path)
    gamma_array = most_common_digit(data)
    epsilon_array = gamma_array ^ True
    return to_decimal(gamma_array) * to_decimal(epsilon_array)


def calculate_metric(data, selector, column_no=0):
    column = data[:, column_no]
    filtered_data = data[column == selector(column)]
    return calculate_metric(filtered_data, selector, column_no + 1) if len(filtered_data) > 1 else to_decimal(filtered_data[0])


def part2(path):
    data = read_data(path)
    oxygen = calculate_metric(data, most_common_digit)
    co2 = calculate_metric(data, least_common_digit)
    return oxygen * co2


if __name__ == "__main__":
    print(f"{part2(sys.argv[1])} result of multiplying position")

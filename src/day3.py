import sys
import numpy as np


def read_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            digits = [int(digit) for digit in list(line.strip())]
            data.append(digits)
    return np.array(data)

to_decimal_array = np.array([2048,1024,512,256,128,64,32,16, 8, 4, 2, 1])

def to_decimal(arr):
    return (arr*to_decimal_array).sum()

def main(path):
    data = read_data(path)
    gamma_array = data.mean(axis=0).round().astype('int')
    epsilon_array = gamma_array ^ True
    return to_decimal(gamma_array) * to_decimal(epsilon_array)


if __name__ == "__main__":
    print(f"{main(sys.argv[1])} result of multiplying position")

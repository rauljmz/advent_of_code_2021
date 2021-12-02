import sys
from functools import reduce
from typing import Iterable

def count_increases(values: Iterable):
    return reduce(lambda a, y: (y, a[1] + 1 if a[0] is not None and y > a[0] else a[1]), values, (None, 0))[1]

def window3(values: Iterable):
    return list(map(lambda x,y,z: x+y+z, values, values[1:], values[2:]))

def main(path):
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(int(line))
    
    return count_increases(window3(data))

if __name__ == "__main__":
    print(f"{main(sys.argv[1])} are increasing over the previous")
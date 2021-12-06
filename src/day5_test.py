import day5
import numpy as np

test_file_path = "./data/day5/test.txt"

class TestDay5:
    def test_part_1_returns_5(self):
        assert day5.part1(test_file_path) == 5

    def test_load_data_returns_array_of_shape_10_2_2(self):
        assert day5.load_points(test_file_path).shape == (10,2,2)


import day8

test_file_path = "./data/day8/test.txt"


class TestDay8:
    def test_part1_returns_26(self):
        assert day8.part1(test_file_path) == 26


    def test_load_data_returns_array_shape_x_10_14(self):
        assert day8.load_data(test_file_path).shape == (10,14)
import day7

test_file_path = "./data/day7/test.txt"


class TestDay7:
    def test_part1_returns_37(self):
        assert day7.part1(test_file_path) == 37

    def test_part2_returns_168(self):
        assert day7.part2(test_file_path) == 168

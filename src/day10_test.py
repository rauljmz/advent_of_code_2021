import day10

test_file_path = "./data/day10/test.txt"

class TestDay10:
    def test_part1_returns_26397(self):
        assert day10.part1(test_file_path) == 26397

    def test_part2_returns_288957(self):
        assert day10.part2(test_file_path) == 288957
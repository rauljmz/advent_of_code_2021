import day6
import pytest

test_file_path = "./data/day6/test.txt"


class TestDay6:
    def test_count_fish_18_days_is_26(self):
        assert day6.count_fish(test_file_path, 18) == 26

    def test_count_fish_80_days_is_5934(self):
        assert day6.count_fish(test_file_path, 80) == 5934

    @pytest.mark.parametrize("expected_count, initial_state,days", [
        (2, 3, 4),
        (1, 3, 3),
        (4, 3, 13),
        (2, 0, 1),
        (2, 1, 8),
        (2, 2, 8),
        (3, 1, 10),
    ])
    def test_count_from_single_fish(self, expected_count, initial_state, days):
        assert day6.count_from_single_fish(
            initial_state, days) == expected_count

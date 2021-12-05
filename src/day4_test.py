import day4
import numpy as np

test_file_path = "./data/day4/test.txt"

class TestDay4:
    def test_part_1_returns_4512(self):
        assert day4.part1(test_file_path) == 4512

    def test_read_data_returns_27_input_numbers(self):
        bingo = day4.create_bingo_game(test_file_path)
        assert len(bingo.numbers) == 27

    def test_read_data_returns_3_cards(self):
        bingo = day4.create_bingo_game(test_file_path)
        assert bingo.cards.shape == (3,5,5)

    def test_read_input_data_returns_100_cards(self):
        bingo = day4.create_bingo_game("./data/day4/input.txt")
        assert bingo.cards.shape == (100,5,5)
        
    def test_calculate_points(self):
        winner = np.array([[1,2,3],[4,-1,-1],[-1,-1,-1]])
        assert day4.calculate_points(winner, 5) == 50
    
    def test_winner_returns_card_with_all_minus_1_in_single_row(self):
        bingo = day4.Bingo(
            numbers=np.array([]),
            cards=np.array(
            [
                [[1,2],[3,4]],
                [[-1,-1],[3,4]],
            ]
        ))
        assert bingo.winner().sum() == 5

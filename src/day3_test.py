import day3
import numpy 

test_file_path = "./data/day3/test.txt"

class TestDay3:
    def test_read_data_returns_array_of_12_elements(self):
        assert len(day3.read_data(test_file_path)) == 12

    def test_read_data_returns_numpy_array(self):
        assert isinstance(day3.read_data(test_file_path), numpy.ndarray)
    
    def test_read_data_returns_numpy_array_of_dimensions_12x2(self):
        assert day3.read_data(test_file_path).shape == (12,5)

    def test_sample_data_returns_150(self):
        assert day3.main(test_file_path) == 198
import day1

class TestDay1CountIncreases:
    def test_empty_iterator_returns_0(self):
        assert day1.count_increases([]) == 0

    def test_1_element_returns_0(self):
        assert day1.count_increases([1]) == 0

    def test_2_element_returns_1(self):
        assert day1.count_increases([1,2]) == 1

    def test_3_element_returns_2(self):
        assert day1.count_increases([1,2,3]) == 2

    def test_3_element_returns_1(self):
        assert day1.count_increases([1,2,0]) == 1

    def test_4_element_returns_2(self):
        assert day1.count_increases([1,2,0,1]) == 2

    def test_4_element_returns_3(self):
        assert day1.count_increases([1,2,3,4]) == 3

    def test_4_element_returns_0(self):
        assert day1.count_increases([4,3,2,1]) == 0

    def test_5_element_returns_0(self):
        assert day1.count_increases([1,10,2,3]) == 2

    def test_sample_input_returns_(self):
        assert day1.count_increases([199,200,208,210,200,207,240,269,260,263]) == 7

class TestDay1SlidingWindow3:
    def test_aggregates_array_3_values(self):
        assert day1.window3([1,2,3]) == [6]
 
    def test_aggregates_array_4_values(self):
        assert day1.window3([1,2,3,4]) == [6,9]

    def test_aggregates_array_6_values(self):
        assert day1.window3([1,2,3,0,0,2]) == [6,5,3,2]

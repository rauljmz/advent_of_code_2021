import pytest
from day18 import Number

class TestNumber:
    st_input = "[[[[[9,8],1],2],3],4]"
    
    def test_number_can_be_created_and_printed(self):
        number = Number(self.st_input)
        assert str(number) == self.st_input

    @pytest.mark.parametrize("st_number, st_exploded", [
        ( st_input, "[[[[0,9],2],3],4]"),
        ( "[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ( "[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ( "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ( "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
    ])
    def test_exploding_numbers(self, st_number, st_exploded):
        number = Number(st_number)
        number.explode()
        assert str(number) == st_exploded

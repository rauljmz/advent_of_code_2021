import pytest
from day18 import Number, add_sequence

class TestNumber:
    @pytest.mark.parametrize("st_number", [
        "[1,0]",
        "[1,[2,3]]",
        "[[2,3],1]",
        "[[2,3],[2,3]]",
        "[[2,[0,1]],[2,3]]",
        "[[[[4,0],[5,4]],[[7,7],[6,5]]],[[[5,5],[0,6]],[[6,5],[5,5]]]]"
    ])
    def test_number_can_be_created_and_printed(self, st_number):
        number = Number.parse(st_number)
        assert str(number) == st_number

    @pytest.mark.parametrize("st_number, st_exploded", [
        ( "[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ( "[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ( "[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ( "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
        ( "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
    ])
    def test_exploding_numbers(self, st_number, st_exploded):
        number = Number.parse(st_number)
        assert str(number) == st_exploded

    @pytest.mark.parametrize("st_number, st_split", [
        ( "[[[[0,7],4],[15,[6,4]]],[1,1]]", 
          "[[[[0,7],4],[[7,8],[6,4]]],[1,1]]"),
    ])
    def test_splitting_numbers(self, st_number, st_split):
        number = Number.parse(st_number)
        assert str(number) == st_split

    @pytest.mark.parametrize("st_number, st_split", [
        ( "[[[[0,7],4],[15,[0,13]]],[1,1]]", 
          "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
    ])
    def test_exploding_and_splitting_numbers(self, st_number, st_split):
        number = Number.parse(st_number)
        assert str(number) == st_split

    @pytest.mark.parametrize("st_number1,st_number2,st_result", [
        (
            "[[[[4,3],4],4],[7,[[8,4],9]]]",
            "[1,1]",
            "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
        ),
        ( "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
        ),(
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]"
        )])
    def test_addition(self, st_number1, st_number2, st_result):
        n1 = Number.parse(st_number1)
        result = n1 + st_number2 
        assert str(result) == st_result

class TestAddSequence:
    def test_sequence_of_4_numbers(self):
        sequence = [
            "[1,1]",
            "[2,2]",
            "[3,3]",
            "[4,4]",
            "[5,5]",
            "[6,6]",
        ]
        result = add_sequence(sequence)
        assert str(result) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"

    def stest_sequence_of_more_numbers(self):
        sequence = [
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
            "[7,[5,[[3,8],[1,4]]]]",
            "[[2,[2,2]],[8,[8,1]]]",
            "[2,9]",
            "[1,[[[9,3],9],[[9,0],[0,7]]]]",
            "[[[5,[7,4]],7],1]",
            "[[[[4,2],2],6],[8,7]]",
        ]
        result = add_sequence(sequence)
        assert str(result) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
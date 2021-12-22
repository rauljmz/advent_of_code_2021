import pytest
from day18 import Number, add_sequence, largest_magnitude


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
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
         "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
        ("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]",
         "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
    ])
    def test_exploding_numbers(self, st_number, st_exploded):
        number = Number.parse(st_number)
        assert str(number) == st_exploded

    @pytest.mark.parametrize("st_number, st_split", [
        ("[[[[0,7],4],[15,[6,4]]],[1,1]]",
         "[[[[0,7],4],[[7,8],[6,4]]],[1,1]]"),
    ])
    def test_splitting_numbers(self, st_number, st_split):
        number = Number.parse(st_number)
        assert str(number) == st_split

    @pytest.mark.parametrize("st_number, st_split", [
        ("[[[[0,7],4],[15,[0,13]]],[1,1]]",
         "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
    ])
    def test_exploding_and_splitting_numbers(self, st_number, st_split):
        number = Number.parse(st_number)
        assert str(number) == st_split

    @pytest.mark.parametrize("st_number,magnitude", [
        ("[9,1]", 29),
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488)
    ])
    def test_magnitude_of_numbers(self, st_number, magnitude):
        number = Number.parse(st_number)
        assert number.magnitude() == magnitude

    @pytest.mark.parametrize("st_number1,st_number2,st_result", [
        (
            "[[[[4,3],4],4],[7,[[8,4],9]]]",
            "[1,1]",
            "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
        ),
        ("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
         ), (
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]"
         ), (
            "[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]",
            "[7,[5,[[3,8],[1,4]]]]",
            "[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]"
        )])
    def test_addition(self, st_number1, st_number2, st_result):
        n1 = Number.parse(st_number1)
        result = n1 + st_number2
        assert str(result) == st_result


class TestSequenceOperations:
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

    def test_sequence_of_more_numbers(self):
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
        assert str(
            result) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
   
    def test_largest_magnitude_of_adding_two_numbers(self):
        sequence = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
        ]
        assert largest_magnitude(sequence) == 3993
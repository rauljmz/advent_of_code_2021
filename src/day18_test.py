from day18 import Number

class TestNumber:
    st_input = "[[[[[9,8],1],2],3],4]"
    
    def test_number_can_be_created_and_printed(self):
        number = Number(self.st_input)
        assert str(number) == self.st_input

    def xtest_explode_number(self):
        number = Number(self.st_input)
        number.explode()
        assert str(number) == "[[[[0,9],2],3],4]"
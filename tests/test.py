from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 3) == 8

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 7) == 3

    def test_division_success(self):
        assert self.calc.division(self, 30, 2) == 15

    def test_multiply_success(self):
        assert self.calc.multiply(self, 6, 7) == 42

    def teardown(self):
        print('Выполнение метода Teardown')

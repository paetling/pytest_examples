import pytest

from pytest_examples.class_to_test import ClassToTest

@pytest.fixture
def any_fit():
    return ClassToTest()

class TestAdd:
    def test_add_strings(self, anyFit):
        with pytest.raises(TypeError):
            anyFit.add("1", "2")

    def test_add_arrays(self, anyFit):
        with pytest.raises(TypeError):
            anyFit.add([1,2,3], 1)

    def test_add_ints(self, anyFit):
        assert anyFit.add(1, 2) == 3
        assert anyFit.add(-1, 2) == 1
        assert anyFit.add(0, 0) == 0

    def test_add_floats(self, anyFit):
        assert anyFit.add(1.2, 2.1) == pytest.approx(3.3)
        assert anyFit.add(-1.1, 2.1) == pytest.approx(1)
        assert anyFit.add(0.0, 1.5) == pytest.approx(1.5)

    def test_add_floats_and_int(self, anyFit):
        assert anyFit.add(1, 2.1) == pytest.approx(3.1)


class TestMultiple:
    def test_multiple_string(self, anyFit):
        with pytest.raises(TypeError):  
            anyFit.multiply("2", "3")  

    def test_multiple_arrays(self, anyFit):
        with pytest.raises(TypeError): 
            anyFit.multiply([3, 4, 5], 1)

    def test_multiple_ints(self, anyFit):
        assert anyFit.multiply(2, 3) == 6
        assert anyFit.multiply(3, 3) == 9
        assert anyFit.multiply(6, 2) == 12
        assert anyFit.multiply(-1, 3) == -3
        assert anyFit.multiply(0, 3) == 0
        assert anyFit.multiply(-3, -4) == 12 

    def test_multiple_floats(self, anyFit):
        assert anyFit.multiply(1.2, 2.1) == pytest.approx(2.52)
        assert anyFit.multiply(-1.1, 2.1) == pytest.approx(-2.31)
        assert anyFit.multiply(0.0, 1.5) == pytest.approx(0)

    def test_multiple_floats_and_int(self, anyFit): 
        assert anyFit.multiply(1, 2.1) == pytest.approx(2.1)      



class TestDivide:
    def test_divide_string(self, anyFit):
        with pytest.raises(TypeError):
            anyFit.divide("5", "6")

    def test_divide_array(self, anyFit):
        with pytest.raises(TypeError):
            anyFit.divide([1, 6, 7], [6, 7, 8])

    def test_divide_int(self, anyFit):
        assert anyFit.divide(4, 2) == 2
        assert anyFit.divide(10, 2) == 5
        assert anyFit.divide(6, 2) == 3
        assert anyFit.divide(0, 10) == 0
        assert anyFit.divide(-2, 10) == -0.2
        with pytest.raises(ZeroDivisionError):
             anyFit.divide(6, 0)

    def test_divide_floats(self, anyFit):
        assert anyFit.divide(0.0, 1.5) == pytest.approx(0)

    def test_divide_floats_and_int(self, anyFit):
        assert anyFit.multiply(1, 2.1) == pytest.approx(2.1)



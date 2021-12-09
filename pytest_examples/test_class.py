import pytest

from pytest_examples.class_to_test import ClassToTest

from freezegun import freeze_time

import datetime

@pytest.fixture
def any_fit():
    return ClassToTest()


@freeze_time("2021-12-09")
class TestGetCurrent(ClassToTest):
    def test_current_time(self):
        assert datetime.datetime.now() == datetime.datetime(2021, 12, 9)



class TestAdd:
    def test_add_strings(self):
        instance = ClassToTest()
        with pytest.raises(TypeError):
            instance.add("1", "2")

    def test_add_arrays(self):
        instance = ClassToTest()
        with pytest.raises(TypeError):
            instance.add([1,2,3], 1)

    def test_add_ints(self):
        instance = ClassToTest()
        assert instance.add(1, 2) == 3
        assert instance.add(-1, 2) == 1
        assert instance.add(0, 0) == 0

    def test_add_floats(self):
        instance = ClassToTest()
        assert instance.add(1.2, 2.1) == pytest.approx(3.3)
        assert instance.add(-1.1, 2.1) == pytest.approx(1)
        assert instance.add(0.0, 1.5) == pytest.approx(1.5)

    def test_add_floats_and_int(self):
        instance = ClassToTest()
        assert instance.add(1, 2.1) == pytest.approx(3.1)


class TestMultiple:
    def test_multiple_string(self, any_fit):
        with pytest.raises(TypeError):  
            any_fit.multiply("2", "3")  

    def test_multiple_arrays(self, any_fit):
        with pytest.raises(TypeError): 
            any_fit.multiply([3, 4, 5], 1)

    def test_multiple_ints(self, any_fit):
        assert any_fit.multiply(2, 3) == 6
        assert any_fit.multiply(3, 3) == 9
        assert any_fit.multiply(6, 2) == 12
        assert any_fit.multiply(-1, 3) == -3
        assert any_fit.multiply(0, 3) == 0
        assert any_fit.multiply(-3, -4) == 12 

    def test_multiple_floats(self, any_fit):
        assert any_fit.multiply(1.2, 2.1) == pytest.approx(2.52)
        assert any_fit.multiply(-1.1, 2.1) == pytest.approx(-2.31)
        assert any_fit.multiply(0.0, 1.5) == pytest.approx(0)

    def test_multiple_floats_and_int(self, any_fit): 
        assert any_fit.multiply(1, 2.1) == pytest.approx(2.1)      



class TestDivide:
    def test_divide_string(self, any_fit):
        with pytest.raises(TypeError):
            any_fit.divide("5", "6")

    def test_divide_array(self, any_fit):
        with pytest.raises(TypeError):
            any_fit.divide([1, 6, 7], [6, 7, 8])

    def test_divide_int(self, any_fit):
        assert any_fit.divide(4, 2) == 2
        assert any_fit.divide(10, 2) == 5
        assert any_fit.divide(6, 2) == 3
        assert any_fit.divide(0, 10) == 0
        assert any_fit.divide(-2, 10) == -0.2
        with pytest.raises(ZeroDivisionError):
             any_fit.divide(5, 0)

    def test_divide_floats(self, any_fit):
        assert any_fit.divide(0.0, 1.5) == pytest.approx(0)

    def test_divide_floats_and_int(self, any_fit):
        assert any_fit.multiply(1, 2.1) == pytest.approx(2.1)




